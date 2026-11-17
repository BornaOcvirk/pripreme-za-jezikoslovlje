"""P7 primjeri: PMI, tf-idf, korak skip-grama, znakovni n-grami (fastText)."""
import math
import numpy as np

# PMI(grčka, rusija) s predavanja
N, c_w, c_c, c_wc = 1415250, 176, 216, 3
pmi = math.log2((c_wc / N) / ((c_w / N) * (c_c / N)))
print(f"PMI(grčka, rusija) = {pmi:.2f}")
print(f"PMI za P(w,c)=0,002 i P(w)P(c)=0,0005: {math.log2(0.002 / 0.0005):.0f}; "
      f"za umnožak 0,004: {math.log2(0.002 / 0.004):.0f} -> PPMI = 0")

# Kosinus ne ovisi o duljini vektora
v, w = np.array([1, 0, 2]), np.array([2, 0, 4])
print("cos([1,0,2],[2,0,4]) =", round(v @ w / (np.linalg.norm(v) * np.linalg.norm(w)), 3),
      "| skalarni umnožak =", v @ w)

# tf-idf
tf = lambda count: math.log10(count + 1)
idf = lambda n_docs, df: math.log10(n_docs / df)
print(f"tf(11) = {tf(11):.2f}, tf(9) = {tf(9):.0f}, idf(je: 248/249) = {idf(249, 248):.3f}, "
      f"idf(nataliteta: 1/249) = {idf(249, 1):.2f}, idf(u svim dok.) = {idf(249, 249):.0f}")
print(f"tfidf(nataliteta, D1) = {tf(11) * idf(249, 1):.2f}")

# Jedan korak skip-grama (η = 1, y = 1)
w_vec, c_vec, y, eta = np.array([1.0, 0.0]), np.array([0.0, 1.0]), 1, 1
y_hat = 1 / (1 + math.exp(-(c_vec @ w_vec)))
c_new = c_vec - eta * (y_hat - y) * w_vec
w_new = w_vec - eta * (y_hat - y) * c_vec
y_hat_new = 1 / (1 + math.exp(-(c_new @ w_new)))
print(f"skip-gram: ŷ {y_hat:.2f} -> c = {c_new}, w = {w_new}, c·w = {c_new @ w_new:.1f}, ŷ = {y_hat_new:.2f}")

# fastText: znakovni trigrami s oznakama < i >
def trigrams(word):
    w = f"<{word}>"
    return [w[i:i + 3] for i in range(len(w) - 2)]
a, b = trigrams("utakmica"), trigrams("utakmicu")
print(a, "\n", b, "\nzajedničkih:", len(set(a) & set(b)), "od", len(a))

# samoprovjera
assert round(pmi, 2) == 6.80 and round(tf(11) * idf(249, 1), 2) == 2.59
assert list(c_new) == [0.5, 1.0] and round(y_hat_new, 2) == 0.73
assert len(set(a) & set(b)) == 6
