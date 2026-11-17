"""P6 primjeri: značajke, sigmoid, softmax, unakrsna entropija, makro F1."""
import math
import re

FIRST = {"ja", "mi", "me", "mene", "nas", "nam", "moj", "moja",
         "moje", "naš", "naša", "naše", "sam", "smo"}

def features(text):
    words = re.findall(r"\w+", text.lower())
    return [words.count("kako"), int('"' in text), sum(w in FIRST for w in words)]

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

w, b = [1.25, 2.04, -1.14], -0.62            # težine s predavanja
for s in ["NATO je priopćio kako će se pozivnica uputiti.", "Ali, napokon smo uspjeli pobjeći."]:
    x = features(s)
    z = sum(wi * xi for wi, xi in zip(w, x)) + b
    p = sigmoid(z)
    print(f"x = {x}, z = {z:.2f}, σ(z) = {p:.2f} -> {'SETimes' if p > 0.5 else 'hrvatski'}")

# Softmax za tri razreda
def softmax(z):
    e = [math.exp(v) for v in z]
    return [v / sum(e) for v in e]
print("softmax:", [round(p, 2) for p in softmax([-1.09, 1.31, -0.23])])

# Unakrsna entropija za ŷ = σ(0,63) ≈ 0,65
y_hat = sigmoid(0.63)
print(f"L(y=1) = {-math.log(y_hat):.2f}, L(y=0) = {-math.log(1 - y_hat):.2f}")
print(f"model kaže P(SETimes) = 0,9, a rečenica je s weba: L = {-math.log(1 - 0.9):.2f}")

# Zamka točnosti: »uvijek SETimes« (586 SETimes, 450 hrvatski)
tp, fp, fn, tn = 586, 450, 0, 0
P, R = tp / (tp + fp), tp / (tp + fn)
f1_set = 2 * P * R / (P + R)
print(f"uvijek SETimes: točnost = {(tp + tn) / 1036:.3f}, F1(set) = {f1_set:.3f}, "
      f"F1(hr) = 0, makro F1 = {(f1_set + 0) / 2:.3f}")

# samoprovjera
assert round(sigmoid(0.63), 2) == 0.65 and round(sigmoid(-1.76), 2) == 0.15
assert [round(p, 2) for p in softmax([-1.09, 1.31, -0.23])] == [0.07, 0.77, 0.16]
assert round(f1_set, 3) == 0.723
