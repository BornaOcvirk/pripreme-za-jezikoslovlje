"""P5 primjeri: faktor grananja, uzorkovanje, dodaj-k, interpolacija, glupo odstupanje."""
import math
import random
from collections import Counter

# Perpleksija kao faktor grananja (jezik s tri boje)
test = ["crvena"] * 4 + ["plava"]
for name, P in [("A", {"crvena": 1/3, "plava": 1/3, "zelena": 1/3}),
                ("B", {"crvena": 0.8, "plava": 0.1, "zelena": 0.1})]:
    log_p = sum(math.log(P[w]) for w in test)
    print(f"model {name}: PP = {math.exp(-log_p / len(test)):.2f}")

# Uzorkovanje inverznom transformacijom: prva riječ s F(w) >= U
def sample(probs, u):
    F = 0
    for w, p in probs.items():
        F += p
        if u <= F:
            return w
print("U = 0,93 ->", sample({"crvena": 0.8, "plava": 0.1, "zelena": 0.1}, 0.93))

# Mali korpus s predavanja: bigrami s <s> i </s>
corpus = ["ja sam Ana", "Ana ja sam", "ja ne volim zelena jaja i šunku"]
uni, bi = Counter(), Counter()
for s in corpus:
    w = ["<s>"] + s.split() + ["</s>"]
    uni.update(w); bi.update(zip(w, w[1:]))
V, N = len(uni), sum(uni.values())

def p_add_k(word, prev, k):
    return (bi[(prev, word)] + k) / (uni[prev] + k * V)

def p_interp(word, prev, l1=0.3, l2=0.7):            # λ1 + λ2 = 1
    return l1 * uni[word] / N + l2 * bi[(prev, word)] / uni[prev]

def stupid_backoff(word, prev):
    if bi[(prev, word)] > 0:
        return bi[(prev, word)] / uni[prev]
    return 0.4 * uni[word] / N                       # nije vjerojatnost (ne zbraja se u 1)

for k in [1, 0.5, 0.01]:
    print(f"add-k, k={k:<4}: P(sam|Ana) = {p_add_k('sam', 'Ana', k):.3f}, "
          f"P(sam|ja) = {p_add_k('sam', 'ja', k):.3f}")
print(f"interpolacija: P(sam|Ana) = {p_interp('sam', 'Ana'):.3f}")
print(f"glupo odstupanje: S(sam|Ana) = {stupid_backoff('sam', 'Ana'):.3f}")

# Generiranje rečenice bigramima
random.seed(4)
def generate():
    words = ["<s>"]
    while words[-1] != "</s>":
        cands = [w for (p, w) in bi if p == words[-1]]
        words.append(random.choices(cands, weights=[bi[(words[-1], w)] for w in cands])[0])
    return " ".join(words[1:-1])
print("generirano:", [generate() for _ in range(3)])

# samoprovjera
assert sample({"crvena": 0.8, "plava": 0.1, "zelena": 0.1}, 0.93) == "zelena"
assert abs(math.exp(-(4 * math.log(0.8) + math.log(0.1)) / 5) - 1.89) < 0.01
