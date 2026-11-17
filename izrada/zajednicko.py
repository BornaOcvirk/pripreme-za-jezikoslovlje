"""Zajednički dijelovi za sve PDF-ove: fontovi, stilovi, oznake teksta, interaktivni elementi."""
import html
import os
import re
import subprocess
import sys
import textwrap

from reportlab.lib import colors
from reportlab.lib.fonts import addMapping
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, PageTemplate, Paragraph, Spacer,
                                Table, TableStyle, XPreformatted)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROG = os.path.join(ROOT, "programi")
PDF_DIR = os.path.join(ROOT, "pdf")

# shortcut: fontovi iz C:\Windows\Fonts (Arial, Consolas, Segoe UI Symbol); za Linux/macOS treba zamijeniti putanje
FONTS = r"C:\Windows\Fonts"
for name, file in [("Arial", "arial.ttf"), ("Arial-Bold", "arialbd.ttf"), ("Arial-Italic", "ariali.ttf"),
                   ("Arial-BoldItalic", "arialbi.ttf"), ("Mono", "consola.ttf"), ("Mono-Bold", "consolab.ttf"),
                   ("Sym", "seguisym.ttf")]:
    pdfmetrics.registerFont(TTFont(name, os.path.join(FONTS, file)))
for b, i, face in [(0, 0, "Arial"), (1, 0, "Arial-Bold"), (0, 1, "Arial-Italic"), (1, 1, "Arial-BoldItalic")]:
    addMapping("Arial", b, i, face)
for b, i, face in [(0, 0, "Mono"), (1, 0, "Mono-Bold"), (0, 1, "Mono"), (1, 1, "Mono-Bold")]:
    addMapping("Mono", b, i, face)

CMAP = {n: set(pdfmetrics.getFont(n).face.charToGlyph) for n in ("Arial", "Mono", "Sym")}
MISSING = set()
VALID_KEYS = set()          # odredišta koja postoje u PDF-u koji se trenutno izrađuje

def start_pdf(keys):
    """Prije izrade PDF-a: popis svih odredišta, da poveznice unaprijed znaju što postoji."""
    VALID_KEYS.clear(); VALID_KEYS.update(keys)

def fallback(text, font):
    out = []
    for ch in text:
        if ch in "\n\t" or ord(ch) in CMAP[font]:
            out.append(ch)
        elif ord(ch) in CMAP["Sym"]:
            out.append(f'<font name="Sym">{ch}</font>')
        else:
            MISSING.add(ch); out.append(ch)
    return "".join(out)

def fallback_markup(s, font="Arial"):
    return re.sub(r"(<[^>]+>|&[#\w]+;)|([^<&]+)", lambda m: m.group(1) or fallback(m.group(2), font), s)

# ---------- boje i stilovi ----------
ACCENT = colors.HexColor("#1f4e79")
ACCENT2 = colors.HexColor("#2e75b6")
QBG = colors.HexColor("#eef4fb")
GRAY = colors.HexColor("#5a5a5a")
GREEN = colors.HexColor("#1e7d46")
RED = colors.HexColor("#b3261e")
TLDR_BG = colors.HexColor("#fff6dc")
LINK = "#1f6fbf"

base = ParagraphStyle("base", fontName="Arial", fontSize=9.6, leading=13.4, spaceAfter=4)
S = {
    "body": base,
    "big": ParagraphStyle("big", base, fontSize=11.5, leading=16),
    "bullet": ParagraphStyle("bullet", base, leftIndent=14, bulletIndent=4, spaceAfter=2),
    "formula": ParagraphStyle("formula", base, fontSize=10.2, leading=15, alignment=1, backColor=QBG,
                              borderPadding=(4, 6, 4, 6), spaceBefore=4, spaceAfter=8),
    "q": ParagraphStyle("q", base, fontName="Arial-Italic", backColor=QBG, borderColor=ACCENT2, borderWidth=0.6,
                        borderPadding=6, spaceBefore=8, spaceAfter=10, textColor=colors.HexColor("#1b2a3a")),
    "tldr": ParagraphStyle("tldr", base, backColor=TLDR_BG, borderColor=colors.HexColor("#e8c55a"), borderWidth=0.6,
                           borderPadding=6, spaceBefore=6, spaceAfter=10),
    "h0": ParagraphStyle("h0", base, fontName="Arial-Bold", fontSize=19, leading=24, textColor=ACCENT, spaceAfter=8),
    "h1": ParagraphStyle("h1", base, fontName="Arial-Bold", fontSize=12.5, leading=16, textColor=ACCENT,
                         spaceBefore=10, spaceAfter=2),
    "h2": ParagraphStyle("h2", base, fontName="Arial-Bold", fontSize=10.5, leading=14, textColor=ACCENT2,
                         spaceBefore=8, spaceAfter=3),
    "small": ParagraphStyle("small", base, fontSize=8.2, leading=11, textColor=GRAY),
    "cell": ParagraphStyle("cell", base, fontSize=8.4, leading=10.6, spaceAfter=0),
    "code": ParagraphStyle("code", fontName="Mono", fontSize=7.6, leading=9.6, backColor=colors.HexColor("#f4f6f9"),
                           borderPadding=5, spaceBefore=4, spaceAfter=9, leftIndent=2),
    "out": ParagraphStyle("out", fontName="Mono", fontSize=7.6, leading=9.6, backColor=colors.HexColor("#1e2430"),
                          textColor=colors.HexColor("#d7e3f4"), borderPadding=5, spaceBefore=4, spaceAfter=9, leftIndent=2),
}

def esc(s):
    return html.escape(html.unescape(s), quote=False)

def _link(m):
    key, text = m.group(1), m.group(2)
    if key in VALID_KEYS:
        return f'<a href="#{key}" color="{LINK}"><u>{text}</u></a>'
    return f"<i>{text}</i>"            # odredište nije u ovom PDF-u

def inline(s):
    """`kod` -> Mono; [[ključ|tekst]] -> unutarnja poveznica; zamjenski font za simbole."""
    s = re.sub(r"`([^`]+)`", lambda m: f'<font name="Mono" size="8.6" color="#8a1c3c">{esc(m.group(1))}</font>', s)
    s = re.sub(r"\[\[(\w+)\|([^\]]+)\]\]", _link, s)
    return fallback_markup(s)

def P(text, style="body"):
    return Paragraph(inline(text), S[style] if isinstance(style, str) else style)

def code_block(text, style="code", width=112):
    lines = []
    for line in text.rstrip("\n").split("\n"):
        lines += textwrap.wrap(line, width, subsequent_indent="    ", drop_whitespace=False) or [""]
    return XPreformatted(fallback_markup(esc("\n".join(lines)), "Mono"), S[style])

def table(rows, avail):
    data = [[Paragraph(inline(c), S["cell"]) if c else "" for c in r] for r in rows]
    ncol = max(len(r) for r in rows)
    for r in data:
        r += [""] * (ncol - len(r))
    plain = lambda c: re.sub(r"<[^>]+>|`", "", c)
    weights = [min(max(len(plain(r[i])) if i < len(r) else 0 for r in rows), 55) + 5 for i in range(ncol)]
    t = Table(data, colWidths=[avail * w / sum(weights) for w in weights], repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#b8c4d4")),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dbe6f3")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
    ]))
    return [t, Spacer(1, 7)]

def render(text, avail):
    """Oznake: prazan red, '• ' natuknica, '1. ' broj, '$ ' formula, '| a | b |' tablica, ``` kod."""
    out, rows, code = [], [], None
    def flush():
        nonlocal rows
        if rows:
            out.extend(table(rows, avail)); rows = []
    for line in text.split("\n"):
        if code is not None:
            if line.strip() == "```":
                out.append(code_block("\n".join(code))); code = None
            else:
                code.append(line)
            continue
        if line.startswith("| "):
            inner = line.strip()[1:-1]
            rows.append([c.strip() for c in re.split(r"(?<=\s)\|(?=\s)", f" {inner} ")])
            continue
        flush()
        if line.strip() == "```":
            code = []
        elif not line.strip():
            out.append(Spacer(1, 3))
        elif line.startswith("• "):
            out.append(Paragraph(inline(line[2:]), S["bullet"], bulletText="•"))
        elif re.match(r"^\d+\. ", line):
            n, rest = line.split(" ", 1)
            out.append(Paragraph(inline(rest), S["bullet"], bulletText=n))
        elif line.startswith("$ "):
            out.append(P(line[2:], "formula"))
        else:
            out.append(P(line))
    flush()
    return out

# ---------- interaktivni elementi ----------
class Heading(Paragraph):
    """Naslov = knjižna oznaka + odredište poveznice + stavka sadržaja."""
    def __init__(self, text, style, key, level):
        super().__init__(fallback_markup(esc(text)), S[style])
        self._bm = (key, text, level)
        VALID_KEYS.add(key)

class Anchor(Flowable):
    """Nevidljivo odredište poveznice (bez stavke u sadržaju)."""
    def __init__(self, key):
        super().__init__(); self.key = key; VALID_KEYS.add(key)
    def wrap(self, aw, ah):
        return 0, 0
    def draw(self):
        self.canv.bookmarkPage(self.key)

class CheckBox(Flowable):
    def __init__(self, name, label):
        super().__init__(); self.name, self.label = name, label
    def wrap(self, aw, ah):
        return aw, 20
    def draw(self):
        c = self.canv
        c.acroForm.checkbox(name=self.name, tooltip=self.label, x=0, y=6, size=11, buttonStyle="check",
                            borderColor=ACCENT2, fillColor=colors.white, textColor=ACCENT, forceBorder=True,
                            relative=True)
        c.setFont("Arial", 8); c.setFillColor(GRAY); c.drawString(16, 8.5, self.label)

class NotesField(Flowable):
    def __init__(self, name, label="Moje bilješke:", height=70):
        super().__init__(); self.name, self.label, self.h = name, label, height
    def wrap(self, aw, ah):
        self.aw = aw
        return aw, self.h + 14
    def draw(self):
        c = self.canv
        c.setFont("Arial-Bold", 8.5); c.setFillColor(ACCENT); c.drawString(0, self.h + 4, self.label)
        c.acroForm.textfield(name=self.name, tooltip="Bilješke", x=0, y=0, width=self.aw, height=self.h,
                             fieldFlags="multiline", fontName="Helvetica", fontSize=9, borderColor=ACCENT2,
                             fillColor=colors.HexColor("#fbfcfe"), textColor=colors.black, forceBorder=True,
                             relative=True)

class Button(Flowable):
    """Klikabilni okvir s tekstom koji vodi na odredište (cijeli okvir je poveznica)."""
    def __init__(self, text, target, color=ACCENT2, letter=None, width=None, fill=None, align="left"):
        super().__init__()
        self.text, self.target, self.color, self.letter = text, target, color, letter
        self.fixed_w, self.fill, self.align = width, fill or colors.white, align
        self.para = Paragraph(inline(text), ParagraphStyle("btn", base, fontSize=10.5, leading=14))
    def wrap(self, aw, ah):
        self.w = self.fixed_w or aw
        pad = 36 if self.letter else 12
        _, h = self.para.wrap(self.w - pad - 10, ah)
        self.h = h + 14
        return aw, self.h + 6
    def draw(self):
        c = self.canv
        x = 0
        c.setStrokeColor(self.color); c.setFillColor(self.fill); c.setLineWidth(1)
        c.roundRect(x, 3, self.w, self.h, 6, stroke=1, fill=1)
        pad = 12
        if self.letter:
            c.setFillColor(self.color); c.circle(x + 17, 3 + self.h / 2, 10, stroke=0, fill=1)
            c.setFillColor(colors.white); c.setFont("Arial-Bold", 11)
            c.drawCentredString(x + 17, 3 + self.h / 2 - 4, self.letter)
            pad = 36
        self.para.drawOn(c, x + pad, 3 + 7)
        c.linkRect("", self.target, (x, 3, x + self.w, 3 + self.h), relative=1, thickness=0)

class Doc(BaseDocTemplate):
    def __init__(self, path, title, footer, nav=("toc", "sadržaj"), **kw):
        super().__init__(path, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.6 * cm,
                         bottomMargin=1.8 * cm, title=title, author="Priprema za kolokvij (studentski materijali)",
                         **kw)
        self.footer, self.nav = footer, nav
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="f",
                      leftPadding=0, rightPadding=0)      # da tablice i gumbi širine doc.width ne strše
        self.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=self._on_page)])

    def afterFlowable(self, f):
        bm = getattr(f, "_bm", None)
        if bm:
            key, text, level = bm
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(text, key, level=level, closed=level > 0)
            self.notify("TOCEntry", (level, esc(text), self.page, key))

    def _on_page(self, c, doc):
        c.saveState()
        w, _ = A4
        c.setStrokeColor(colors.HexColor("#c9d6e6")); c.setLineWidth(0.5)
        c.line(1.8 * cm, 1.35 * cm, w - 1.8 * cm, 1.35 * cm)
        c.setFont("Arial", 7.8); c.setFillColor(GRAY)
        c.drawString(1.8 * cm, 0.95 * cm, self.footer)
        c.drawRightString(w - 1.8 * cm, 0.95 * cm, f"str. {doc.page}")
        key, label = self.nav
        if key in VALID_KEYS:
            c.setFillColor(colors.HexColor(LINK))
            c.setFont("Sym", 7.8); c.drawCentredString(w / 2 - 17, 0.95 * cm, "▲")
            c.setFont("Arial", 7.8); c.drawString(w / 2 - 12, 0.95 * cm, label)
            c.linkRect("", key, (w / 2 - 25, 0.8 * cm, w / 2 + 40, 1.25 * cm), relative=0, thickness=0)
        c.restoreState()

def run(script):
    """Pokrene program iz mape programi i vrati ispis (pada ako assert ne prođe)."""
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    r = subprocess.run([sys.executable, script], cwd=PROG, capture_output=True, text=True, encoding="utf-8", env=env)
    if r.returncode:
        raise SystemExit(f"{script} nije uspio:\n{r.stderr}")
    return r.stdout

def read_prog(script):
    with open(os.path.join(PROG, script), encoding="utf-8") as f:
        return f.read()
