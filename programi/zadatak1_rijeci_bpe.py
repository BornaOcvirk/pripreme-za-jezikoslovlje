"""Zadatak 1 (P2, V2): pojavnice, različnice i BPE."""
import re
from collections import Counter

# --- 1. clean(text): samo riječi od slova, malim slovima ---
text = ("Na stolu je knjiga, na knjizi je olovka, a na olovki je mrav. "
        "Knjiga je stara, a olovka je nova. Mrav ne čita knjigu.")

def clean(text):
    return [w.lower() for w in re.findall(r"\w+", text) if w.isalpha()]

words = clean(text)
print("N =", len(words), "  |V| =", len(set(words)))     # N = pojavnice, |V| = različnice
print(Counter(words).most_common(5))

# --- 2. BPE: tri spajanja ---
corpus = [list(w) for w in "set new new renew reset renew".split()]   # riječ = lista simbola

def count_pairs(words):
    pairs = Counter()
    for w in words:
        for a, b in zip(w, w[1:]):        # susjedni simboli unutar riječi
            pairs[(a, b)] += 1
    return pairs

def merge(words, pair):
    # zadano: svako pojavljivanje para (a, b) zamijeni jednim simbolom a + b
    out = []
    for w in words:
        new, i = [], 0
        while i < len(w):
            if i + 1 < len(w) and (w[i], w[i + 1]) == pair:
                new.append(w[i] + w[i + 1]); i += 2
            else:
                new.append(w[i]); i += 1
        out.append(new)
    return out

for step in range(3):
    pair, n = count_pairs(corpus).most_common(1)[0]
    corpus = merge(corpus, pair)
    print(step + 1, pair, n, "→", [" ".join(w) for w in corpus])

# samoprovjera: ako se nešto pokvari, program javlja AssertionError
assert (len(words), len(set(words))) == (24, 14)
assert corpus[1] == ["new"] and corpus[3] == ["re", "new"]
