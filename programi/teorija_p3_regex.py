"""P3 primjeri: regularni izrazi, preciznost/odziv, grupe, ELIZA."""
import re

print("raw string:", "a\\tb" == r"a\tb")
print("[a-z]+ :", re.findall(r"[a-z]+", "Računalno"))        # č nije u rasponu a-z
print("\\w+   :", re.findall(r"\w+", "Računalno jezikoslovlje, 2027."))
print("ba*!  :", re.findall(r"ba*!", "ba! baa! baaa!"))
print("baa+! :", re.findall(r"baa+!", "ba! baa! baaa!"))
print("{5}   :", re.findall(r"[0-9]{5}", "31000 Osijek, 10000 Zagreb, tel. 123"))
print("r.ka  :", re.findall(r"r.ka", "ruka rika rijeka"))

s = 'Rekao je "da", pa "ne".'
print("pohlepno   :", re.findall(r'".*"', s))
print("nepohlepno :", re.findall(r'".*?"', s))

# prednost operatora
print("je*       :", re.findall(r"je*", "j je jee jeje"))
print("mačka|ke  :", re.findall(r"mačka|ke", "mačke mačka"))
print("(ha)+ vs ha+:", re.search(r"(ha)+", "hahaha").group(), re.findall(r"ha+", "hahaha"))

# preciznost i odziv za traženje riječi »je«
text = "Je li to jezik? Da, to je jezik koji je lijep."
gold = {m.span() for m in re.finditer(r"\b[jJ]e\b", text)}   # 3 pojavnice riječi je/Je
for pat in [r"je", r"[jJ]e", r"\b[jJ]e\b"]:
    found = [m.span() for m in re.finditer(pat, text)]
    correct = sum(span in gold for span in found)              # ostalo su lažno pozitivni
    print(f"{pat:12} pronađeno {len(found)}, točno {correct}, "
          f"P = {correct}/{len(found)}, R = {correct}/{len(gold)}")

# grupe za hvatanje i zamjena
print(re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\2. \1. \3.", "Datum je 10/15/2011"))
print(re.findall(r"\b(\w+)\s+\1\b", "Rekao je je da dolazi."))      # povratna referenca
print(re.findall(r"(?:ha)+", "hahaha"))                              # grupa bez hvatanja
print(re.findall(r"\d+(?= €)", "Kava 2 €, sok 3 €, 5 komada"))     # pogled unaprijed
print(re.findall(r"(?<=\$)\d+", "cijena $45 i 30 kn"))              # pogled unatrag

# ELIZA: kaskada zamjena
def eliza(t):
    t = t.upper()
    t = re.sub(r"\bMOJ\b", "TVOJ", t)
    t = re.sub(r"\bJA SAM\b", "TI SI", t)
    if re.match(r".*\bTI SI (TUŽAN|TUŽNA)\b", t):
        return re.sub(r".*\bTI SI (TUŽAN|TUŽNA)\b.*", r"ŽAO MI JE ŠTO SI \1.", t)
    if re.match(r".*\bUVIJEK\b", t):
        return "MOŽEŠ LI SE SJETITI PRIMJERA?"
    return "RECI MI NEŠTO VIŠE."

for u in ["Ja sam tužna većinu vremena.", "Uvijek nas zbog nečega gnjave.", "Ja sam umoran."]:
    print(f"{u:35} -> {eliza(u)}")

# samoprovjera
assert re.findall(r"[a-z]+", "Računalno") == ["a", "unalno"]
assert re.findall(r"mačka|ke", "mačke mačka") == ["ke", "mačka"]
assert eliza("Ja sam tužna većinu vremena.") == "ŽAO MI JE ŠTO SI TUŽNA."
