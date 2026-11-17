"""Zadatak 5 (P7, V7): kosinus i PPMI na matrici riječ–kontekst."""
import numpy as np

words = ["kuna", "eura", "ponedjeljak", "utorak"]
contexts = ["milijuna", "milijardi", "oko", "izjavio", "siječnja", "("]
M = np.array([[62, 22, 11, 0, 0, 6],
              [67, 27, 25, 0, 0, 4],
              [0, 0, 0, 10, 7, 40],
              [0, 0, 0, 6, 6, 28]], dtype=float)

def cosine(v, w):
    return v @ w / (np.linalg.norm(v) * np.linalg.norm(w))

print("kuna – eura:       ", round(cosine(M[0], M[1]), 3))
print("kuna – ponedjeljak:", round(cosine(M[0], M[2]), 3))

def ppmi(M):
    N = M.sum()
    p_wc = M / N
    p_w = M.sum(axis=1, keepdims=True) / N      # zbrojevi redaka
    p_c = M.sum(axis=0, keepdims=True) / N      # zbrojevi stupaca
    with np.errstate(divide="ignore"):
        pmi = np.log2(p_wc / (p_w * p_c))       # log2(0) = -inf
    return np.maximum(pmi, 0)                   # PPMI: negativno -> 0

P = ppmi(M)
print(" " * 12, " ".join(f"{c:>9}" for c in contexts))
for word, row in zip(words, P):
    print(f"{word:12}", " ".join(f"{v:9.2f}" for v in row))
print("Najveća težina za 'ponedjeljak':", contexts[P[2].argmax()])

# samoprovjera
assert round(cosine(M[0], M[1]), 3) == 0.985 and round(cosine(M[0], M[2]), 3) == 0.086
assert contexts[P[2].argmax()] == "izjavio" and round(P[2, 3], 2) == 1.82
