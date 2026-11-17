"""Probni kolokvij: rješenja pet novih zadataka (isti stil kao kolokvij_1_priprema.ipynb).

Svaki zadatak počinje oznakom "# === Zadatak N" (po njoj PDF vadi kod pojedinog zadatka).
"""
import math
import re
import unicodedata
from collections import Counter

import numpy as np
from nltk import edit_distance

# === Zadatak 1
print("=== Zadatak 1")
text = "Ana voli jezik. Jezik voli Anu, a Ana voli i jezikoslovlje!"

def clean(text):
    return [w.lower() for w in re.findall(r"\w+", text) if w.isalpha()]

words = clean(text)
print("N =", len(words), " |V| =", len(set(words)), " najčešće:", Counter(words).most_common(3))

for w in ["jezik", "računalno", "čćđšž"]:
    print(f"{w:10} znakova: {len(w)}, bajtova: {len(w.encode('utf-8'))}")

c1, c2 = "č", "č"                       # č kao 1 ili 2 kodne točke
print("jednaki?", c1 == c2, "| nakon NFC:", unicodedata.normalize("NFC", c2) == c1)

corpus = [list(w) for w in "low low lower lowest newest".split()]

def count_pairs(words):
    pairs = Counter()
    for w in words:
        pairs.update(zip(w, w[1:]))
    return pairs

def merge(words, pair):
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

for step in range(2):
    pair, n = count_pairs(corpus).most_common(1)[0]
    corpus = merge(corpus, pair)
    print(step + 1, pair, n, "→", [" ".join(w) for w in corpus])

assert (len(words), len(set(words))) == (11, 7)
assert corpus[2] == ["low", "e", "r"]

# === Zadatak 2
print("=== Zadatak 2")
t = "Kava je 20 kn, a sok 30 kn. Rekao je je da ne ne dolazi. Cijena: 1.250 kn."
amounts = re.findall(r"\d+(?:\.\d{3})*(?= kn)", t)              # pogled unaprijed: bez » kn«
print("iznosi:", amounts)
print("ponovljene riječi:", re.findall(r"\b(\w+)\s+\1\b", t))    # povratna referenca
print(re.sub(r"(\d+(?:\.\d{3})*) kn", r"\1 HRK", t))              # grupa za hvatanje u zamjeni

def table_d(src, tgt, sub_cost=1):
    D = [[0] * (len(tgt) + 1) for _ in range(len(src) + 1)]
    for i in range(1, len(src) + 1):
        D[i][0] = i
    for j in range(1, len(tgt) + 1):
        D[0][j] = j
    for i in range(1, len(src) + 1):
        for j in range(1, len(tgt) + 1):
            z = 0 if src[i - 1] == tgt[j - 1] else sub_cost
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + z)
    return D

D = table_d("mak", "rak")
print("    #  r  a  k")
for ch, row in zip("#mak", D):
    print(ch, " ", "  ".join(map(str, row)))
print("D[3][3] =", D[3][3], "| uz zamjenu = 2:", table_d("mak", "rak", 2)[3][3],
      "| nltk:", edit_distance("mak", "rak"))

assert amounts == ["20", "30", "1.250"] and D[3][3] == 1

# === Zadatak 3
print("=== Zadatak 3")
sents = ["volim jezik", "volim jezikoslovlje", "jezik volim"]
uni, bi = Counter(), Counter()
for s in sents:
    w = ["<s>"] + s.split() + ["</s>"]
    uni.update(w); bi.update(zip(w, w[1:]))
V, N = len(uni), sum(uni.values())

p_mle = lambda w, prev: bi[(prev, w)] / uni[prev]
p_addk = lambda w, prev, k=0.5: (bi[(prev, w)] + k) / (uni[prev] + k * V)
p_interp = lambda w, prev, lam=0.7: lam * p_mle(w, prev) + (1 - lam) * uni[w] / N

def perplexity(sentence, p):
    w = ["<s>"] + sentence.split() + ["</s>"]
    logp = 0
    for prev, word in zip(w, w[1:]):
        prob = p(word, prev)
        if prob == 0:
            return math.inf
        logp += math.log(prob)
    return math.exp(-logp / (len(w) - 1))

print(f"P(jezik|volim) = {p_mle('jezik', 'volim'):.3f}, P(volim|<s>) = {p_mle('volim', '<s>'):.3f}, V = {V}")
for test in ["jezik volim jezik", "jezikoslovlje volim"]:
    print(f"{test:22} MLE: {perplexity(test, p_mle):.3f}  dodaj-0,5: {perplexity(test, p_addk):.3f}"
          f"  interpolacija: {perplexity(test, p_interp):.3f}")

assert round(perplexity("jezik volim jezik", p_mle), 3) == 2.449
assert perplexity("jezikoslovlje volim", p_mle) == math.inf

# === Zadatak 4
print("=== Zadatak 4")
FIRST = {"ja", "mi", "me", "mene", "nas", "nam", "moj", "moja", "moje", "naš", "naša", "naše", "sam", "smo"}

def features(s):
    w = re.findall(r"\w+", s.lower())
    return [w.count("kako"), int('"' in s), sum(x in FIRST for x in w)]

sigmoid = lambda z: 1 / (1 + math.exp(-z))
W, B = [1.25, 2.04, -1.14], -0.62                      # težine s predavanja
for s in ['Ministar je izjavio kako će "uskoro" doći.', "Mi smo napokon stigli kući.", "Kako ste vi?"]:
    x = features(s)
    p = sigmoid(sum(wi * xi for wi, xi in zip(W, x)) + B)
    print(f"{s:45} x = {x}  P(set) = {p:.2f} → {'set' if p > 0.5 else 'hr'}")

w, b, x, y, lr = [0, 0, 0], 0, [0, 0, 1], 0, 0.5        # jedan korak SGD
y_hat = sigmoid(b)
w = [wi - lr * (y_hat - y) * xi for wi, xi in zip(w, x)]
b -= lr * (y_hat - y)
print("nakon koraka: w =", w, "b =", b)

gold = ["set"] * 30 + ["hr"] * 20
pred = ["set"] * 25 + ["hr"] * 5 + ["set"] * 8 + ["hr"] * 12
f1s = []
for cls in ["set", "hr"]:
    tp = sum(g == p == cls for g, p in zip(gold, pred))
    fp = sum(g != cls and p == cls for g, p in zip(gold, pred))
    fn = sum(g == cls and p != cls for g, p in zip(gold, pred))
    P, R = tp / (tp + fp), tp / (tp + fn)
    f1s.append(2 * P * R / (P + R))
    print(f"{cls}: tp={tp} fp={fp} fn={fn}  P={P:.3f} R={R:.3f} F1={f1s[-1]:.3f}")
acc = sum(g == p for g, p in zip(gold, pred)) / len(gold)
print(f"točnost = {acc:.3f}, makro F1 = {sum(f1s) / 2:.3f}")

assert w == [0, 0, -0.25] and b == -0.25 and round(acc, 2) == 0.74

# === Zadatak 5
print("=== Zadatak 5")
docs = ["utakmica je završila neriješeno",
        "trener je nakon utakmice zadovoljan",
        "cijena kruha je porasla",
        "kuna je jača nego prošle godine i cijena je viša"]
vocab = sorted({w for d in docs for w in d.split()})
counts = np.array([[d.split().count(t) for d in docs] for t in vocab], dtype=float)   # riječ × dokument
tf = np.log10(counts + 1)
df = (counts > 0).sum(axis=1)
idf = np.log10(len(docs) / df)
X = tf * idf[:, None]
for t in ["je", "cijena", "utakmica"]:
    print(f"idf({t}) = {idf[vocab.index(t)]:.3f}")

q = np.array([1.0 if t == "utakmica" else 0.0 for t in vocab]) * idf
cos = [(q @ X[:, j]) / (np.linalg.norm(q) * np.linalg.norm(X[:, j])) for j in range(len(docs))]
print("kosinus upita 'utakmica' s dokumentima:", [round(float(c), 3) for c in cos])

N_pairs, c_w, c_c, c_wc = 1000, 20, 50, 5
print(f"PMI = log2({c_wc}·{N_pairs} / ({c_w}·{c_c})) = {math.log2(c_wc * N_pairs / (c_w * c_c)):.2f}")

assert idf[vocab.index("je")] == 0 and cos[1] == 0      # 'utakmice' ≠ 'utakmica' za tf-idf
