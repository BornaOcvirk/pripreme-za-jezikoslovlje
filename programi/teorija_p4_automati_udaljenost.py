"""P4 primjeri: tokenizator za hrvatski, segmentacija, konačni automat, tablica D."""
import re
import nltk

# Tokenizator pravilima: redoslijed alternativa je važan (kratice i datumi prije riječi i brojeva)
pattern = r"""(?xi)
  (?:dr|sc|npr|tj|itd|prof)\.      # kratice
| \d{1,2}\.\s\d{1,2}\.\s\d{4}\.    # datum
| \d+(?:\.\d{3})*(?:,\d+)?         # 1.250,50
| (?:www\.)?\w+(?:\.\w+)+          # web-adrese
| \w+(?:-\w+)*                     # riječi: PDV-a
| [.,;:!?€—()]                     # interpunkcija
"""
text = "Dr. sc. Ana Kovač je 15. 10. 2026. platila 1.250,50 € npr. na www.mathos.hr — i to bez PDV-a!"
print(nltk.regexp_tokenize(text, pattern))

# Segmentacija rečenica: točka je višeznačna
t = "Sastanak je 5. listopada u 10 h. Dr. Horvat kasni. Dođite na vrijeme!"
print(re.split(r"(?<=[.!?])\s+(?=[A-ZČĆĐŠŽ])", t))
print(re.split(r"(?<!\bDr\.)(?<=[.!?])\s+(?=[A-ZČĆĐŠŽ])", t))     # + kratica Dr.

# Deterministički konačni automat za ovčji jezik baa+!
delta = {("q0", "b"): "q1", ("q1", "a"): "q2", ("q2", "a"): "q3",
         ("q3", "a"): "q3", ("q3", "!"): "q4"}

def accepts(s, start="q0", final={"q4"}):
    q = start
    for c in s:
        q = delta.get((q, c))          # None: nema prijelaza -> odbaci
        if q is None:
            return False
    return q in final

for s in ["baa!", "baaaa!", "ba!", "baa"]:
    print(f"{s:7} {'prihvaćen' if accepts(s) else 'odbačen'}")

# Minimalna udaljenost uređivanja s tablicom D i povratnim tragom
def min_edit_distance(source, target, sub_cost=1):
    n, m = len(source), len(target)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = i                                  # i brisanja
    for j in range(1, m + 1):
        D[0][j] = j                                  # j umetanja
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            z = 0 if source[i - 1] == target[j - 1] else sub_cost
            D[i][j] = min(D[i - 1][j] + 1,           # brisanje
                          D[i][j - 1] + 1,           # umetanje
                          D[i - 1][j - 1] + z)       # zamjena
    return D

def backtrace(D, source, target, sub_cost=1):
    i, j, pairs = len(source), len(target), []
    while i > 0 or j > 0:
        z = 0 if i and j and source[i - 1] == target[j - 1] else sub_cost
        if i and j and D[i][j] == D[i - 1][j - 1] + z:
            pairs.append((source[i - 1], target[j - 1])); i -= 1; j -= 1
        elif i and D[i][j] == D[i - 1][j] + 1:
            pairs.append((source[i - 1], "*")); i -= 1       # brisanje
        else:
            pairs.append(("*", target[j - 1])); j -= 1       # umetanje
    return pairs[::-1]

src, tgt = "pjesma", "pisma"
D = min_edit_distance(src, tgt)
print("\n    #  " + "  ".join(tgt))
for i, row in enumerate(D):
    print(("#" + src)[i], " ", "  ".join(str(v) for v in row))
print("udaljenost:", D[-1][-1], "| poravnanje:", backtrace(D, src, tgt))
print("intention -> execution:", min_edit_distance("intention", "execution")[-1][-1],
      "| zamjena = 2:", min_edit_distance("intention", "execution", 2)[-1][-1])
print("hrvatksi -> hrvatski:", nltk.edit_distance("hrvatksi", "hrvatski"),
      "| s transpozicijom:", nltk.edit_distance("hrvatksi", "hrvatski", transpositions=True))

# samoprovjera
assert accepts("baaa!") and not accepts("ba!")
assert D[-1][-1] == 2 and min_edit_distance("intention", "execution", 2)[-1][-1] == 8
assert min_edit_distance("kuča", "kuća")[-1][-1] == 1
