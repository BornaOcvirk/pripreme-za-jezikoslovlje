"""Zadatak 2 (P3-P4, V3-V4): datumi regularnim izrazom i ispravljanje pogrešaka."""
import re
from collections import Counter
from nltk import edit_distance

# --- 1. datumi 2026-10-15 -> 15. 10. 2026. ---
news = ("Sjednica je održana 2026-10-15 u Zagrebu, a sljedeća je zakazana za 2026-11-12 u Osijeku. "
        "Rok za prijave bio je 2026-09-30 u podne.")

dates = re.findall(r"\d{4}-\d{2}-\d{2}", news)
print(dates)
hr = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3. \2. \1.", news)   # grupe 1, 2, 3 = godina, mjesec, dan
print(hr)

# --- 2. najbliža riječ iz rječnika; kod jednake udaljenosti češća ---
freq = Counter({"jezik": 120, "je": 5000, "jež": 3, "predsjednik": 300, "predsjednica": 40,
                "sveučilište": 80, "sveučilišta": 60, "hrvatski": 400, "hrvatska": 900})

def suggest(word):
    return min(freq, key=lambda w: (edit_distance(word, w), -freq[w]))   # najbliža, pa češća

results = {}
for word in ["jezk", "predsjedik", "sveučilšte", "hrvatksi"]:
    best = suggest(word)
    results[word] = best
    print(f"{word:12} → {best:12} (udaljenost {edit_distance(word, best)})")

# samoprovjera
assert dates == ["2026-10-15", "2026-11-12", "2026-09-30"]
assert "15. 10. 2026." in hr
assert results == {"jezk": "jezik", "predsjedik": "predsjednik",
                   "sveučilšte": "sveučilište", "hrvatksi": "hrvatski"}
