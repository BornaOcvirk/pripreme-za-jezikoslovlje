"""Zadatak 4 (P6, V6): jedan korak gradijentnog spusta i matrica zabune."""
import math
from collections import Counter

# --- 1. sigmoid, predict, jedan korak ---
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def predict(w, b, x):
    return sigmoid(sum(wi * xi for wi, xi in zip(w, x)) + b)    # σ(w·x + b)

def loss(w, b, x, y):                                            # unakrsna entropija
    y_hat = predict(w, b, x)
    return -math.log(y_hat) if y == 1 else -math.log(1 - y_hat)

w, b, x, y, lr = [0, 0, 0], 0, [1, 0, 0], 1, 0.1
loss_before = loss(w, b, x, y)
print("prije:", w, b, "ŷ =", predict(w, b, x), "gubitak =", round(loss_before, 4))

y_hat = predict(w, b, x)
w = [wi - lr * (y_hat - y) * xi for wi, xi in zip(w, x)]        # gradijent (ŷ − y)·x_j
b = b - lr * (y_hat - y)
loss_after = loss(w, b, x, y)
print("poslije:", w, b, "ŷ =", round(predict(w, b, x), 4), "gubitak =", round(loss_after, 4))

# --- 2. matrica zabune za razred "set" ---
gold = ["set"] * 40 + ["hr"] * 10 + ["set"] * 40 + ["hr"] * 30
pred = ["set"] * 40 + ["set"] * 10 + ["hr"] * 40 + ["hr"] * 30

counts = Counter(zip(gold, pred))      # (zlatna, sustav) -> broj
tp, fp = counts[("set", "set")], counts[("hr", "set")]
fn, tn = counts[("set", "hr")], counts[("hr", "hr")]
print("tp, fp, fn, tn =", tp, fp, fn, tn)

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)
accuracy = (tp + tn) / len(gold)
print(f"P = {precision:.3f}, R = {recall:.3f}, F1 = {f1:.3f}, točnost = {accuracy:.3f}")

# samoprovjera
assert w == [0.05, 0, 0] and b == 0.05
assert round(loss_before, 4) == 0.6931 and round(loss_after, 4) == 0.6444
assert (tp, fp, fn, tn) == (40, 10, 40, 30) and round(f1, 3) == 0.615
