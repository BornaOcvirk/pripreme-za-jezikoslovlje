"""P2 primjeri: pojavnice/različnice, UTF-8, normalizacija, BPE koder."""
import re
import unicodedata

# Pojavnice i različnice (primjer s predavanja)
s = "Na stolu je knjiga, na knjizi je olovka, a na olovki je mrav."
tokens = re.findall(r"\w+", s.lower())
print("N =", len(tokens), " |V| =", len(set(tokens)))

# UTF-8: č = U+010D = 2 bajta (110yyyyy 10xxxxxx)
c = "č"
print(f"kodna točka: U+{ord(c):04X}, bajtovi: {c.encode('utf-8')}, "
      f"binarno: {' '.join(f'{b:08b}' for b in c.encode('utf-8'))}")
w = "računalno"
print(f"'{w}': {len(w)} znakova, {len(w.encode('utf-8'))} bajtova")
for ch in "ač进😀":
    print(f"  {ch!r}: U+{ord(ch):04X} -> {len(ch.encode('utf-8'))} bajt(a)")

# Zamka: isti izgled, različiti stringovi; rješenje NFC
nfc = "č"          # č kao jedna kodna točka
nfd = "č"         # c + kvačica (kombinirajući znak)
print("isti izgled:", nfc, nfd, "| jednaki?", nfc == nfd,
      "| nakon NFC:", unicodedata.normalize("NFC", nfd) == nfc)
print("lj je", len("lj"), "kodne točke, iako je jedno slovo abecede")

# BPE koder: naučena spajanja primjenjujemo istim redom (slajd »BPE koder«)
MERGES = [("n", "e"), ("ne", "w"), ("▁", "r"), ("▁r", "e"),
          ("▁", "new"), ("▁re", "new"), ("s", "e"), ("se", "t")]

def bpe_encode(word):
    symbols = ["▁"] + list(word)            # ▁ = razmak ispred riječi
    for a, b in MERGES:                      # redoslijed iz učenja, ne frekvencija
        i, out = 0, []
        while i < len(symbols):
            if i + 1 < len(symbols) and (symbols[i], symbols[i + 1]) == (a, b):
                out.append(a + b); i += 2
            else:
                out.append(symbols[i]); i += 1
        symbols = out
    return symbols

for word in ["resets", "newer", "anew"]:
    print(f"{word:7} -> {bpe_encode(word)}")

# samoprovjera
assert (len(tokens), len(set(tokens))) == (13, 9)
assert c.encode("utf-8") == b"\xc4\x8d" and len(w.encode("utf-8")) == 10
assert bpe_encode("resets") == ["▁re", "set", "s"]
assert bpe_encode("anew") == ["▁", "a", "new"]
