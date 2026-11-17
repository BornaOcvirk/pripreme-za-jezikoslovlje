"""Izrađuje sva tri PDF-a u mapi pdf/.

    python izrada/napravi_pdfove.py

Programe iz mape programi/ pokreće sam (moraju proći svoje assert provjere) i u PDF upisuje njihov stvarni ispis.
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import CondPageBreak, Flowable, PageBreak, Paragraph, Spacer, Table, TableStyle
from reportlab.platypus.tableofcontents import TableOfContents

import zajednicko as Z
from zajednicko import P, S, base, render
from sadrzaj_teorija import FORMULAS, GITHUB, GITHUB_KOL, TOPICS
from sadrzaj_ukratko import INTROS, TLDR
from sadrzaj_kolokvij1 import STATEMENTS, TASKS
from sadrzaj_kviz import MCQ, PROBNI

FOOT = "I051 Računalno jezikoslovlje · studentska priprema za kolokvij"

def title_page(kicker, title, subtitle):
    return [Spacer(1, 3 * cm),
            Paragraph(kicker, ParagraphStyle("k", base, fontSize=12, textColor=Z.ACCENT2)),
            Paragraph(Z.fallback_markup(title), ParagraphStyle("t", base, fontName="Arial-Bold", fontSize=28,
                                                                leading=34, textColor=Z.ACCENT, spaceBefore=6)),
            Paragraph(Z.fallback_markup(subtitle), ParagraphStyle("s", base, fontSize=12.5, leading=18, spaceBefore=6)),
            Spacer(1, 1 * cm)]

def toc_block():
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle("toc0", base, fontName="Arial-Bold", fontSize=10.5, leading=15, textColor=Z.ACCENT, spaceBefore=5),
        ParagraphStyle("toc1", base, fontSize=9, leading=12, leftIndent=14),
    ]
    return [Paragraph('<a name="toc"/>Sadržaj', S["h0"]), toc, PageBreak()]

RUN_HOWTO = r"""<b>Pokretanje programa (VS Code)</b>
1. File → Open Folder… → otvori mapu repozitorija.
2. Ctrl+Shift+P → »Python: Select Interpreter« → odaberi Python 3.
3. U terminalu (Terminal → New Terminal) jednom instaliraj pakete: `pip install -r requirements.txt`
4. Otvori program iz mape `programi/` i klikni ▶ (Run Python File) gore desno, ili u terminalu:
```
cd programi
python zadatak1_rijeci_bpe.py
```
Svaki program na kraju ima `assert` provjere: ako ne javi `AssertionError`, rezultati su točni. Ako se č, ć … u terminalu prikazuju krivo, u PowerShellu upiši `$env:PYTHONIOENCODING="utf-8"`."""

# =====================================================================================
def build_teorija():
    keys = {"toc", "tf", "ti"} | {t[0] for t in TOPICS} | {q[0] for t in TOPICS for q in t[3]}
    Z.start_pdf(keys)
    path = os.path.join(Z.PDF_DIR, "1_teorija_odgovori.pdf")
    doc = Z.Doc(path, "Teorija za 1. kolokvij – odgovori (P2–P7)", FOOT)
    W = doc.width
    st = title_page("I051 Računalno jezikoslovlje · 1. kolokvij",
                    "Teorija bez panike ☕",
                    "Svih 30 teorijskih pitanja (P2–P7) s odgovorima. Svako pitanje ima i žuti okvir "
                    "»ukratko« za kad ti se ne čita sve.")
    st += render(r"""<b>Kako koristiti</b>
• Sadržaj je klikabilan, a lijevo u pregledniku su i knjižne oznake. Na dnu svake stranice »▲ sadržaj« te vraća gore.
• <b>Žuti okvir</b> je verzija za brzo ponavljanje. Ispod njega je cijeli odgovor, otprilike onakav kakav bi napisao/la na kolokviju.
• Kvačica <b>»naučeno«</b> uz svako pitanje i polje za bilješke na kraju teme ostaju zapamćeni kad spremiš PDF (Ctrl+S). Rade u Edgeu, Chromeu, Firefoxu i Adobe Readeru.
• Svaka tema ima i program s primjerima u mapi `programi/`, pa slobodno promijeni brojeve i vidi što se dogodi.
• Kad misliš da znaš, provjeri se u PDF-u <b>2_kviz_i_probni_kolokvij.pdf</b>. 😉""", W)
    st.append(PageBreak())
    st += toc_block()

    for tkey, ttitle, demo, questions in TOPICS:
        st.append(Z.Heading(ttitle, "h0", tkey, 0))
        st.append(P(INTROS[tkey], "big"))
        st.append(P(f"Kod za igranje: `programi/{demo}`", "small"))
        for i, (qkey, qtitle, qtext, answer) in enumerate(questions, 1):
            st.append(CondPageBreak(5 * cm))
            st.append(Z.Heading(f"{tkey[1]}.{i} {qtitle}", "h1", qkey, 1))
            st.append(Z.CheckBox(f"naučeno_{qkey}", "naučeno, kvačica kad ovo znaš objasniti nekom drugom"))
            st.append(P("<b>Pitanje.</b> " + Z.esc(qtext), "q"))
            st.append(P("☕ <b>Ukratko:</b> " + TLDR[qkey], "tldr"))
            st += render(answer, W)
        st += [Spacer(1, 8), Z.NotesField(f"bilješke_{tkey}"), PageBreak()]

    st.append(Z.Heading("Formule na jednom mjestu (šalabahter za učenje, ne za kolokvij 😇)", "h0", "tf", 0))
    st += Z.table([["pojam", "formula"]] + [[a, b] for a, b in FORMULAS], W)
    st.append(Spacer(1, 10))
    st.append(Z.Heading("Izvori", "h0", "ti", 0))
    st += render(rf"""• Vježbe i materijali za kolokvij (profesorov GitHub): <a href="{GITHUB}" color="{Z.LINK}"><u>{GITHUB}</u></a> · <a href="{GITHUB_KOL}" color="{Z.LINK}"><u>kolokvij</u></a>
• Predavanja P2–P7 (slajdovi s kolegija): odgovori prate njihove primjere i brojke (korpus UD Croatian SET).
• Jurafsky &amp; Martin, <i>Speech and Language Processing</i>, 3. izd. (nacrt 2026.), pogl. 2–5 i 11.
• Pitanja: `kolokvij_1_pitanja.docx` (mapa kolokvij na GitHubu).
Ovo su studentski materijali; ako nađeš grešku, javi ili otvori issue. 🙂""", W)
    # pokreni demo programe da PDF upućuje samo na provjeren kod
    for _, _, demo, _ in TOPICS:
        Z.run(demo)
    doc.multiBuild(st)
    return path

# =====================================================================================
def build_kolokvij1():
    keys = {"toc", "t0"} | {z[0] for z in TASKS}
    Z.start_pdf(keys)
    path = os.path.join(Z.PDF_DIR, "3_kolokvij1_rjesenja.pdf")
    doc = Z.Doc(path, "Kolokvij 1 – rješenja i objašnjenja", FOOT)
    W = doc.width
    st = title_page("I051 Računalno jezikoslovlje · kolokvij_1_priprema.ipynb",
                    "Kolokvij 1: rješenja",
                    "Pet zadataka iz pripreme za kolokvij: model-odgovor na teorijsko pitanje, objašnjenje "
                    "praktičnog dijela korak po korak, kod i stvarni ispis.")
    st += render(r"""<b>Kako je složeno</b>
• Svaki zadatak: <b>teorijsko pitanje</b> → odgovor (dug otprilike koliko treba na kolokviju) → <b>praktični zadatak</b> → objašnjenje → kod → ispis (crni okvir, stvarni izlaz programa).
• Kod je u mapi `programi/` (`zadatak1_…py` do `zadatak5_…py`). Najbolje: prvo pokušaj sam/a u bilježnici, pa usporedi.
• Kvačica »riješeno« uz svaki zadatak pamti se kad spremiš PDF.""", W)
    st.append(PageBreak())
    st += toc_block()
    st.append(Z.Heading("Kako pokrenuti kod", "h1", "t0", 0))
    st += render(RUN_HOWTO, W)
    st.append(PageBreak())

    for zkey, ztitle, script, _, expl in TASKS:
        theory_q, practical, answer = STATEMENTS[zkey]
        st.append(Z.Heading(ztitle, "h0", zkey, 0))
        st.append(Z.CheckBox(f"riješeno_{zkey}", "riješeno, kvačica kad zadatak znaš riješiti bez gledanja"))
        st.append(P("<b>Teorijsko pitanje.</b> " + theory_q, "q"))
        st.append(P("<b>Odgovor</b>", "h2"))
        st += render(answer, W)
        st.append(CondPageBreak(4 * cm))
        st.append(P("<b>Praktični zadatak</b>", "h2"))
        st += render(practical, W)
        st.append(P("<b>Objašnjenje rješenja</b>", "h2"))
        st += render(expl.split("\n\n", 1)[1], W)          # prvi odlomak upućivao je na PDF s teorijom
        st.append(P(f"<b>Kod</b> · `programi/{script}`", "h2"))
        st.append(Z.code_block(Z.read_prog(script)))
        st.append(P(f"<b>Ispis</b> · `python {script}`", "h2"))
        st.append(Z.code_block(Z.run(script), "out"))
        st.append(PageBreak())
    doc.multiBuild(st)
    return path

# =====================================================================================
class Progress(Flowable):
    def __init__(self, k, n):
        super().__init__(); self.k, self.n = k, n
    def wrap(self, aw, ah):
        self.aw = aw
        return aw, 10
    def draw(self):
        c = self.canv
        c.setFillColor(colors.HexColor("#e3e9f2")); c.roundRect(0, 2, self.aw, 6, 3, stroke=0, fill=1)
        c.setFillColor(Z.ACCENT2); c.roundRect(0, 2, self.aw * self.k / self.n, 6, 3, stroke=0, fill=1)

YES = ["Točno! 🎉", "Bingo! ✔", "Tako je! 💪", "Pogodak! 🎯", "Bravo! ✔"]
NO = ["Ups, nije to. 🙈", "Skoro… ali ne. 😕", "Nope. 😅", "Ne baš. 🤔"]

def build_kviz():
    n = len(MCQ)
    keys = {"start", "mapa", "kraj", "probni"}
    keys |= {f"k{i}" for i in range(1, n + 1)} | {f"k{i}_da" for i in range(1, n + 1)} | {f"k{i}_ne" for i in range(1, n + 1)}
    keys |= {f"p{i}" for i in range(1, 6)} | {f"p{i}_r" for i in range(1, 6)}
    Z.start_pdf(keys)
    path = os.path.join(Z.PDF_DIR, "2_kviz_i_probni_kolokvij.pdf")
    doc = Z.Doc(path, "Kviz i probni kolokvij – 1. kolokvij", FOOT, nav=("mapa", "mapa kviza"))
    W = doc.width
    half = (W - 12) / 2

    def two(a, b):
        t = Table([[a, b]], colWidths=[half + 6, half + 6], hAlign="LEFT")
        t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
        return t

    st = [Z.Anchor("start")]
    st += title_page("I051 Računalno jezikoslovlje · 1. kolokvij",
                     "Kviz + probni kolokvij 🎮",
                     f"{n} pitanja s ponuđenim odgovorima (P2–P7) i probni kolokvij od 5 zadataka, "
                     "sve klikabilno.")
    st += render(r"""<b>Pravila igre</b>
• Klikni na odgovor. Ako je točan, dobiješ objašnjenje i ideš dalje; ako nije, dobiješ pomoć i pokušaš ponovno.
• Na stranici s točnim odgovorom označi kvačicu <b>»iz prve«</b> ako si pogodio/la bez pomoći. Na kraju prebroji kvačice (i spremi PDF s Ctrl+S, pa vidiš napredak).
• Na dnu svake stranice »▲ mapa kviza« vodi na popis svih pitanja.
• Radi u svakom pregledniku PDF-a (Edge, Chrome, Firefox, Adobe), jer je sve napravljeno običnim poveznicama, bez skripti.""", W)
    st.append(Spacer(1, 10))
    st.append(two(Z.Button("<b>Kreni s kvizom →</b>", "k1", fill=colors.HexColor("#eaf3fc"), width=half),
                  Z.Button("<b>Probni kolokvij →</b>", "probni", width=half)))
    st.append(Z.Button("Mapa pitanja", "mapa", width=half))
    st.append(PageBreak())

    # mapa pitanja
    st.append(Z.Anchor("mapa"))
    st.append(Paragraph("Mapa kviza", S["h0"]))
    st.append(P("Klikni broj za skok na pitanje."))
    by_topic = {}
    for i, q in enumerate(MCQ, 1):
        by_topic.setdefault(q[0], []).append(i)
    bw = (W - 5 * 6) / 6
    for topic, idx in by_topic.items():
        st.append(P(f"<b>{topic}</b>", "h2"))
        row = [Z.Button(f"<b>{i}</b>", f"k{i}", width=bw) for i in idx] + [""] * (6 - len(idx))
        t = Table([row], colWidths=[bw + 6] * 6, hAlign="LEFT")
        t.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 6)]))
        st.append(t)
    st.append(Spacer(1, 12))
    st.append(two(Z.Button("<b>Probni kolokvij →</b>", "probni", width=half), Z.Button("Na početak", "start", width=half)))
    st.append(PageBreak())

    # pitanja
    for i, (topic, q, opts, ok, hint, why) in enumerate(MCQ, 1):
        opts = [f"`{o}`" if o.startswith("[") else o for o in opts]   # Pythonove liste u fontu za kod
        nxt =f"k{i + 1}" if i < n else "kraj"
        st += [Z.Anchor(f"k{i}"),
               Z.Heading(f"Pitanje {i}/{n}", "h1", f"k{i}_h", 0),
               P(topic, "small"), Progress(i, n), Spacer(1, 10),
               P(q, "big"), Spacer(1, 10)]
        for j, opt in enumerate(opts):
            st.append(Z.Button(opt, f"k{i}_da" if j == ok else f"k{i}_ne", letter="ABCD"[j]))
        st += [Spacer(1, 6), P("Klikni na odgovor. (Bez varanja! 👀)", "small"), PageBreak()]

        st += [Z.Anchor(f"k{i}_da"),
               Paragraph(Z.fallback_markup(YES[i % len(YES)]), ParagraphStyle("yes", S["h0"], textColor=Z.GREEN)),
               P(f"Pitanje {i}: {q}", "small"),
               P(f"<b>Točan odgovor: {'ABCD'[ok]}) {opts[ok]}</b>", "tldr"),
               P(why), Spacer(1, 6),
               Z.CheckBox(f"iz_prve_{i}", "iz prve, bez pomoći"), Spacer(1, 8),
               two(Z.Button("<b>Sljedeće pitanje →</b>" if i < n else "<b>Kraj kviza →</b>", nxt,
                            fill=colors.HexColor("#eaf7ef"), color=Z.GREEN, width=half),
                   Z.Button("Mapa kviza", "mapa", width=half)),
               PageBreak()]

        st += [Z.Anchor(f"k{i}_ne"),
               Paragraph(Z.fallback_markup(NO[i % len(NO)]), ParagraphStyle("no", S["h0"], textColor=Z.RED)),
               P(f"Pitanje {i}: {q}", "small"),
               P("💡 <b>Pomoć:</b> " + hint, "tldr"), Spacer(1, 8),
               two(Z.Button("<b>← Pokušaj ponovno</b>", f"k{i}", color=Z.RED, fill=colors.HexColor("#fdeeee"), width=half),
                   Z.Button("Pokaži rješenje", f"k{i}_da", width=half)),
               PageBreak()]

    st += [Z.Anchor("kraj"), Paragraph(Z.fallback_markup("Kraj kviza! 🏁"), S["h0"]),
           P(f"Prebroji kvačice »iz prve«. Okvirno: {n - 3}+ odlično, {n - 10}+ solidno, a ispod toga ponovi teme "
             "u kojima si griješio/la (PDF <b>1_teorija_odgovori.pdf</b>).", "big"), Spacer(1, 10),
           two(Z.Button("<b>Probni kolokvij →</b>", "probni", width=half), Z.Button("Ponovno od početka", "k1", width=half)),
           PageBreak()]

    # probni kolokvij
    src = Z.read_prog("probni_kolokvij.py")
    code_parts = re.split(r"(?m)^# === Zadatak ", src)[1:]       # samo oznake na početku retka, ne u docstringu
    out_parts = Z.run("probni_kolokvij.py").split("=== Zadatak ")[1:]
    st += [Z.Anchor("probni"), Z.Heading("Probni kolokvij", "h0", "probni_h", 0)]
    st += render(r"""Pet <b>novih</b> zadataka u istom stilu kao kolokvij: teorijsko pitanje + kratak program.
• Postavi si sat na <b>60 minuta</b>. Teoriju piši na papir, a kod u VS Codeu (npr. nova datoteka `programi/moj_probni.py`).
• Potrebni paketi: `numpy` i `nltk`, isti kao na vježbama.
• Tek kad završiš, klikni »Rješenje →«. Cijelo rješenje je u `programi/probni_kolokvij.py`.""", W)
    st.append(Spacer(1, 8))
    for i, (title, *_rest) in enumerate(PROBNI, 1):
        st.append(Z.Button(title, f"p{i}", letter=str(i)))
    st.append(PageBreak())

    for i, (title, theory, practical, answer, notes) in enumerate(PROBNI, 1):
        nxt = f"p{i + 1}" if i < 5 else "start"
        st += [Z.Anchor(f"p{i}"), Z.Heading(f"Probni {title}", "h1", f"p{i}_h", 0),
               Z.CheckBox(f"probni_riješeno_{i}", "riješeno"),
               P("<b>Teorijsko pitanje.</b> " + theory, "q"),
               P("<b>Praktični zadatak</b>", "h2")]
        st += render(practical, W)
        st += [Spacer(1, 10),
               two(Z.Button("<b>Rješenje →</b>", f"p{i}_r", color=Z.GREEN, fill=colors.HexColor("#eaf7ef"), width=half),
                   Z.Button("Sljedeći zadatak" if i < 5 else "Na početak", nxt, width=half)),
               PageBreak()]
        code = "# (importi su na vrhu datoteke programi/probni_kolokvij.py)\n" + code_parts[i - 1].split("\n", 1)[1]
        st += [Z.Anchor(f"p{i}_r"), Paragraph(f"Rješenje: {title}", S["h1"]),
               P("<b>Teorija: model-odgovor</b>", "h2")]
        st += render(answer, W)
        st.append(P("<b>Praktični dio: što primijetiti</b>", "h2"))
        st += render(notes, W)
        st += [P("<b>Kod</b>", "h2"), Z.code_block(code.strip()),
               P("<b>Ispis</b>", "h2"), Z.code_block(out_parts[i - 1].split("\n", 1)[1], "out"),
               two(Z.Button("← Natrag na zadatak", f"p{i}", width=half),
                   Z.Button("<b>Sljedeći zadatak →</b>" if i < 5 else "<b>Na početak</b>", nxt, width=half)),
               PageBreak()]
    doc.build(st)
    return path

if __name__ == "__main__":
    os.makedirs(Z.PDF_DIR, exist_ok=True)
    for build in (build_teorija, build_kviz, build_kolokvij1):
        print("Gotovo:", build())
    if Z.MISSING:
        print("UPOZORENJE: znakovi bez glifa:", "".join(sorted(Z.MISSING)))
