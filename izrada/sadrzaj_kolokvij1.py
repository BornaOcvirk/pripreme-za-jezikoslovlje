"""Kolokvij 1 (kolokvij_1_priprema.ipynb): objašnjenja praktičnih dijelova zadataka."""

# ---------------------------------------------------------------------------------------
# Kolokvijski zadaci (kolokvij_1_priprema.ipynb): objašnjenje + pokretanje
TASKS = [
("z1", "Zadatak 1. Riječi i tokeni (P2, V2)", "zadatak1_rijeci_bpe.py", "q1_1",
 r"""<b>Teorijsko pitanje:</b> razlika između različnice i pojavnice, Heapsov zakon i zašto hrvatski ima više različnica, odgovoreno u [[q1_1|pitanju 1.1]].

<b>Praktični dio 1: `clean(text)`.</b> `re.findall(r"\w+", text)` vraća sve nizove riječnih znakova (\w u Pythonu 3 obuhvaća i č, ć, đ, š, ž). Uvjet `w.isalpha()` izbacuje nizove sa znamenkama, a `.lower()` izjednačava »Knjiga« i »knjiga«. Zatim:
• N = `len(words)`: broj <b>pojavnica</b>;
• |V| = `len(set(words))`: skup uklanja ponavljanja, pa je to broj <b>različnica</b>;
• `Counter(words).most_common(5)`: pet najčešćih riječi.
Rezultat: N = 24, |V| = 14. Najčešća je »je« (5 puta), zatim »na« (3).

<b>Praktični dio 2: BPE.</b> Svaka riječ je lista simbola (`list("renew")` → ['r','e','n','e','w']). `count_pairs` za svaku riječ uparuje susjedne simbole s `zip(w, w[1:])` i broji ih u `Counter`. Parovi se broje samo <b>unutar</b> riječi, jer BPE ne spaja preko granica riječi. U petlji tri puta uzmemo najčešći par (`most_common(1)[0]`) i spojimo ga funkcijom `merge`.
• 1. spajanje: (n, e), 4 pojave (new ×2, renew ×2)
• 2. spajanje: (ne, w), 4 pojave, pa nastaje token »new«
• 3. spajanje: (r, e), 3 pojave (renew ×2, reset)
Parovi (n, e) i (e, w) oba imaju 4 pojave. `most_common` tada vraća par koji je prvi prebrojen. Na predavanju je treće spajanje bilo ▁ + r, jer je tamo korpus imao oznaku ▁ za početak riječi."""),
("z2", "Zadatak 2. Regularni izrazi i udaljenost uređivanja (P3–P4, V3–V4)", "zadatak2_regex_levenshtein.py", "q3_5",
 r"""<b>Teorijsko pitanje:</b> Levenshteinova udaljenost, dinamičko programiranje, D[i, j], početni uvjeti i rekurzivna relacija, odgovoreno u [[q3_5|pitanju 3.5]].

<b>Praktični dio 1: datumi.</b> Uzorak `\d{4}-\d{2}-\d{2}` traži točno 4 znamenke, crticu, 2 znamenke, crticu i 2 znamenke. `re.findall` vraća sva tri datuma. Za preoblikovanje dijelove stavimo u <b>grupe za hvatanje</b> `(\d{4})-(\d{2})-(\d{2})`: grupa 1 je godina, 2 mjesec, 3 dan. U zamjeni ih preslažemo: `r"\3. \2. \1."` → »15. 10. 2026.«. Zamjena je sirovi string, inače bi Python `\1` protumačio kao znak s kodom 1.

<b>Praktični dio 2: ispravljanje pogrešaka.</b> `min(freq, key=…)` prolazi kroz sve riječi rječnika i bira onu s najmanjim ključem. Ključ je par `(edit_distance(word, w), -freq[w])`. Python uspoređuje parove leksikografski: prvo udaljenost (manja je bolja), a kod jednake udaljenosti `-freq` (manji, tj. veća frekvencija, je bolji). Tako dobivamo »najbližu, pa češću«.
• jezk → jezik (1 umetanje), predsjedik → predsjednik (1), sveučilšte → sveučilište (1)
• hrvatksi → hrvatski je <b>2</b>: zamjena susjednih slova (ks → sk) za Levenshteina su dvije zamjene. Uz `transpositions=True` (Damerau) bila bi 1. Kandidat »hrvatska« je dalje (3)."""),
("z3", "Zadatak 3. N-gramski jezični modeli (P5, V5)", "zadatak3_ngrami.py", "q4_3",
 r"""<b>Teorijsko pitanje:</b> perpleksija, zašto je manja bolja i zašto MLE daje beskonačnu perpleksiju, odgovoreno u [[q4_3|pitanju 4.3]] i [[q4_5|pitanju 4.5]] (Laplace).

<b>Praktični dio 1: brojanje i MLE.</b> Svakoj rečenici dodamo `<s>` i `</s>`. `unigrams.update(words)` broji riječi, a `bigrams.update(zip(words, words[1:]))` parove susjednih riječi. MLE: `p_mle(w, prev) = C(prev w) / C(prev)`.
• P(sam | ja) = C(ja sam)/C(ja) = 2/3 = <b>0,667</b>
• P(Ana | `<s>`) = C(`<s>` Ana)/C(`<s>`) = 1/3 = <b>0,333</b>

<b>Praktični dio 2: Laplace i perpleksija.</b> V = `len(unigrams)` = 11 različnica (uključujući `<s>` i `</s>`). Laplace: (C(prev w) + 1) / (C(prev) + V). Perpleksija zbraja log-vjerojatnosti (zbog potkoračenja) i dijeli s brojem predviđanja n = 4 (Ana, sam, ja, `</s>`; `<s>` se ne predviđa):
$ PP = exp( −(1/n) Σ log P(w<sub>i</sub>|w<sub>i−1</sub>) )
• <b>MLE: ∞.</b> Bigram (Ana, sam) ne postoji u korpusu, pa je P = 0 i funkcija odmah vraća `math.inf`.
• <b>Laplace: 11,34.</b> P(Ana|`<s>`) = 2/14, P(sam|Ana) = 1/13, P(ja|sam) = 1/13, P(`</s>`|ja) = 1/14; PP = (2/14 · 1/13 · 1/13 · 1/14)<super>−1/4</super> ≈ 11,34."""),
("z4", "Zadatak 4. Klasifikacija teksta i logistička regresija (P6, V6)", "zadatak4_logisticka_regresija.py", "q5_3",
 r"""<b>Teorijsko pitanje:</b> unakrsna entropija, gradijentni spust, stopa učenja i gradijent (ŷ − y)·x<sub>j</sub>, odgovoreno u [[q5_3|pitanju 5.3]].

<b>Praktični dio 1: jedan korak gradijentnog spusta.</b> `predict` računa z = Σ w<sub>i</sub>x<sub>i</sub> + b (skalarni umnožak preko `zip`) i vraća σ(z). `loss` je unakrsna entropija: −log ŷ za y = 1, a −log(1 − ŷ) za y = 0.
• Prije: w = [0, 0, 0], b = 0, pa z = 0, ŷ = 0,5 i gubitak = −ln 0,5 = <b>0,6931</b>.
• Gradijent: (ŷ − y)·x = −0,5 · [1, 0, 0] = [−0,5, 0, 0]; za pomak −0,5.
• Korak (η = 0,1): w = w − η·gradijent = [0,05, 0, 0], b = 0,05.
• Poslije: z = 0,1, ŷ = 0,525, gubitak = <b>0,6444</b>. Gubitak se smanjio, a promijenila se samo težina prisutne značajke.

<b>Praktični dio 2: matrica zabune.</b> `Counter(zip(gold, pred))` broji parove (zlatna oznaka, odluka sustava):
• tp = (set, set) = 40; fp = (hr, set) = 10 (sustav je rekao set 50 puta, 10 pogrešno)
• fn = (set, hr) = 40 (u testu je 80 rečenica iz SETimesa, pronađeno 40); tn = (hr, hr) = 30
P = 40/50 = <b>0,800</b>, R = 40/80 = <b>0,500</b>, F1 = 2·0,8·0,5/1,3 = <b>0,615</b>, točnost = 70/120 = 0,583. Preciznost je visoka, ali klasifikator pronalazi tek polovicu rečenica iz SETimesa, a F1 kao harmonijska sredina to kažnjava."""),
("z5", "Zadatak 5. Vektorska semantika (P7, V7)", "zadatak5_vektori.py", "q6_2",
 r"""<b>Teorijsko pitanje:</b> kosinus umjesto skalarnog umnoška, česte riječi, PMI i PPMI, odgovoreno u [[q6_2|pitanju 6.2]].

<b>Praktični dio 1: kosinus.</b> `v @ w` je skalarni umnožak, a `np.linalg.norm` duljina vektora. kuna–eura = 5047/(66,97·76,54) = <b>0,985</b> (isti konteksti: milijuna, milijardi, oko); kuna–ponedjeljak = <b>0,086</b> (zajednički je samo kontekst »(«).

<b>Praktični dio 2: PPMI.</b> Funkcija prati formulu točno:
• N = `M.sum()`: zbroj svih ćelija;
• P(w, c) = `M / N`; P(w) = zbrojevi <b>redaka</b> / N (`axis=1`); P(c) = zbrojevi <b>stupaca</b> / N (`axis=0`);
• `keepdims=True` čuva oblik stupca (4×1) i retka (1×6), pa `p_w * p_c` daje matricu 4×6 svih umnožaka (numpy broadcasting);
• `np.log2(…)` daje PMI; za ćelije s 0 dobije se log 0 = −∞ (`errstate` utišava upozorenje), a `np.maximum(pmi, 0)` sve negativno i −∞ pretvara u 0.
<b>Zaključak:</b> za »ponedjeljak« najveću težinu ima <b>izjavio</b> (1,82), a ne »(« (1,53), iako je zagrada s 40 pojavljivanja daleko najčešći kontekst. Zagrada se pojavljuje i uz »kunu« i »euro«, pa je manje specifična za dane, dok se »izjavio« u ovoj matrici pojavljuje samo uz dane. PPMI dakle ne nagrađuje učestalost, nego <b>neobičnu</b> učestalost uz baš tu riječ. Vrijednosti »nemogućih« parova (kuna – izjavio) su 0."""),
]

# Tekst zadataka iz bilježnice (teorijsko pitanje, praktični zadatak) i kratki model-odgovor na teoriju,
# napisan otprilike onoliko dugo koliko stane u odgovor na kolokviju.
STATEMENTS = {
"z1": (r"""Objasnite razliku između <b>različnice</b> i <b>pojavnice</b>. Što kaže <b>Heapsov zakon</b> i zašto tekst na hrvatskom ima više različnica od engleskog teksta iste duljine?""",
r"""1. Napišite funkciju `clean(text)` koja vraća listu riječi teksta: samo riječi od slova, malim slovima. Za zadani tekst izračunajte N, |V| i pet najčešćih riječi.
2. <b>BPE.</b> Riječi malog korpusa s predavanja rastavljene su na znakove. Napišite funkciju `count_pairs(words)` koja broji parove susjednih simbola (unutar riječi) i pomoću zadane funkcije `merge` napravite <b>tri spajanja</b> algoritma BPE. Nakon svakog spajanja ispišite spojeni par i novi rastav riječi.""",
r"""<b>Pojavnica</b> je svako pojavljivanje riječi u tekstu (njihov broj je N), a <b>različnica</b> je svaka različita riječ (skup različnica je rječnik V, broj |V|). U rečenici »Na stolu je knjiga, na knjizi je olovka, a na olovki je mrav.« ima N = 13 pojavnica i |V| = 9 različnica (»na« i »je« po 3 puta; »knjiga« i »knjizi« su dvije različnice).
<b>Heapsov zakon:</b> |V| = k · N<super>β</super>, uz 0 &lt; β &lt; 1 (za engleski β ≈ 0,44–0,56). Rječnik raste s duljinom teksta i nikad ne prestaje rasti, jer sadržajne riječi (imena, nazivi) stalno pristižu. Zato u novom tekstu uvijek ima nepoznatih riječi.
<b>Hrvatski</b> ima bogatu fleksiju (padeži, rod, broj, glagolski oblici), pa jedna lema ima mnogo oblika (knjiga, knjige, knjizi, knjigu, knjigom …), a svaki oblik je zasebna različnica. Zato uz isti N hrvatski tekst ima više različnica od engleskog; u korpusu SET oblika je gotovo dvaput više nego lema."""),
"z2": (r"""Definirajte <b>Levenshteinovu udaljenost</b>. Zašto se računa <b>dinamičkim programiranjem</b>? Što je D[i, j], koji su početni uvjeti i kako glasi rekurzivna relacija?""",
r"""1. Iz zadanog teksta regularnim izrazom izdvojite sve datume u obliku `2026-10-15` i funkcijom `re.sub` s grupama za hvatanje pretvorite ih u hrvatski zapis `15. 10. 2026.`
2. Za svaku pogrešno napisanu riječ predložite najbližu riječ iz zadanog rječnika (funkcija `edit_distance` iz NLTK-a). Kad je više riječi jednako blizu, uzmite češću.""",
r"""<b>Levenshteinova udaljenost</b> je najmanji broj operacija uređivanja (umetanje, brisanje, zamjena znaka) kojima se jedan string pretvara u drugi; svaka operacija košta 1, a »zamjena« istim znakom 0 (pjesma → pisma = 2; u inačici sa zamjenom 2 bilo bi 3).
<b>Dinamičko programiranje:</b> nizova operacija ima eksponencijalno mnogo, ali se podproblemi preklapaju, jer mnogo putova vodi do istog para prefiksa. Svaki podproblem riješimo jednom i spremimo u tablicu, pa je složenost O(n·m).
<b>D[i, j]</b> je udaljenost između prvih i znakova izvora X i prvih j znakova cilja Y; rješenje je D[n, m].
<b>Početni uvjeti:</b> D[i, 0] = i (i brisanja), D[0, j] = j (j umetanja).
$ D[i, j] = min( D[i−1, j] + 1,  D[i, j−1] + 1,  D[i−1, j−1] + z ),   z = 0 ako X[i] = Y[j], inače 1
Prvi član je brisanje, drugi umetanje, treći zamjena. Povratnim tragom (pamtimo odakle smo došli) dobivamo i poravnanje."""),
"z3": (r"""Definirajte <b>perpleksiju</b> i objasnite zašto je manja perpleksija bolja. Zašto bigramski model procijenjen bez izglađivanja (MLE) može na testnom skupu imati beskonačnu perpleksiju i kako to rješava <b>Laplaceovo izglađivanje</b>?""",
r"""Zadan je mali korpus s predavanja.
1. Prebrojite unigrame i bigrame (rečenicama dodajte `<s>` i `</s>`) i izračunajte MLE vjerojatnosti P(sam | ja) i P(Ana | `<s>`).
2. Napišite `p_laplace(word, prev)` i izračunajte perpleksiju testne rečenice <i>Ana sam ja</i> s MLE-om i s Laplaceovim izglađivanjem. Vjerojatnost računajte zbrajanjem logaritama.""",
r"""<b>Perpleksija</b> je inverz vjerojatnosti testnog skupa, normaliziran brojem riječi (geometrijska sredina):
$ PP(W) = P(w<sub>1:N</sub>)<super>−1/N</super> = <super>N</super>√( ∏ 1 / P(w<sub>i</sub>|w<sub>i−1</sub>) )
N je broj predviđanja (riječi i `</s>`). <b>Manja je bolja</b> jer veća vjerojatnost testa znači manju perpleksiju: model je manje »iznenađen«. Tumači se kao težinski faktor grananja, tj. između koliko jednako vjerojatnih riječi model u prosjeku bira (model koji svakoj od 4 boje daje 1/4 ima PP = 4).
<b>Beskonačnost:</b> MLE (C(w<sub>n−1</sub>w<sub>n</sub>)/C(w<sub>n−1</sub>)) daje vjerojatnost 0 svakom bigramu kojeg nema u skupu za učenje. Dovoljan je jedan takav bigram u testu: umnožak je 0, a PP = 1/0 = ∞ (na SET-u 31 % testnih bigrama nije viđeno).
<b>Laplace</b> svakom broju dodaje 1: P = (C(w<sub>n−1</sub>w<sub>n</sub>) + 1) / (C(w<sub>n−1</sub>) + V). Nijedna vjerojatnost više nije 0, pa je PP konačna. Cijena: viđeni bigrami gube mnogo vjerojatnosti (uz velik V model može biti lošiji i od unigramskog), pa su bolji dodaj-k ili interpolacija."""),
"z4": (r"""Kako glasi <b>unakrsna entropija</b> za binarnu logističku regresiju? Objasnite <b>gradijentni spust</b>, ulogu stope učenja η i protumačite gradijent (ŷ − y)·x<sub>j</sub>.""",
r"""1. Napišite `sigmoid(z)` i `predict(w, b, x)` te napravite <b>jedan korak</b> gradijentnog spusta za primjer s predavanja: x = [1, 0, 0], y = 1, početne težine i pomak 0, η = 0,1. Ispišite gubitak prije i poslije koraka.
2. Klasifikator je 50 rečenica pripisao SETimesu, od kojih je 40 točno; u testu je 80 rečenica iz SETimesa. Iz zadanih lista zlatnih oznaka i odluka izračunajte matricu zabune, preciznost, odziv i F1 za razred `set`.""",
r"""Model daje ŷ = σ(<b>w</b>·<b>x</b> + b) = P(y = 1 | x). <b>Unakrsna entropija</b> je negativni logaritam vjerojatnosti koju model daje točnoj oznaci:
$ L<sub>CE</sub>(ŷ, y) = −[ y log ŷ + (1 − y) log(1 − ŷ) ]
(za y = 1: −log ŷ; za y = 0: −log(1 − ŷ)). Savršen model ima gubitak 0, a samouvjerena pogreška velik.
<b>Gradijentni spust</b> traži težine s najmanjim gubitkom: u svakom koraku težine malo pomaknemo <b>suprotno od gradijenta</b>, jer je to smjer najbržeg pada gubitka: w ← w − η · ∂L/∂w.
<b>Stopa učenja η</b> određuje veličinu koraka; to je hiperparametar. Prevelika preskače minimum, a premalena čini učenje presporim.
$ ∂L/∂w<sub>j</sub> = (ŷ − y) · x<sub>j</sub>,     ∂L/∂b = ŷ − y
<b>Tumačenje:</b> (ŷ − y) je pogreška modela. Što više griješi, to je korak veći, a kad je točan, težine se gotovo ne mijenjaju. Množi se vrijednošću značajke, pa se težina značajke koje nema u primjeru (x<sub>j</sub> = 0) ne mijenja. Ako je ŷ &lt; y, gradijent je negativan i težina raste (npr. x = [1, 0, 0], y = 1, η = 0,1: w<sub>1</sub> = 0,05)."""),
"z5": (r"""Zašto za sličnost vektora riječi koristimo <b>kosinus</b>, a ne skalarni umnožak? Zašto česte riječi kvare vektore iz brojanja? Definirajte <b>PMI</b> i <b>PPMI</b> i protumačite ih.""",
r"""Zadana je matrica riječ–kontekst s predavanja (korpus SET, prozor ±4, šest stupaca).
1. Napišite funkciju `cosine(v, w)` i izračunajte kosinus za parove <i>kuna–eura</i> i <i>kuna–ponedjeljak</i>.
2. Napišite funkciju `ppmi(M)` po formuli s predavanja (vjerojatnosti iz zbrojeva retka, stupca i cijele matrice) i ispišite matricu PPMI zaokruženu na dvije decimale. Koji kontekst ima najveću težinu za <i>ponedjeljak</i> i zašto?""",
r"""<b>Kosinus:</b> skalarni umnožak <b>v</b>·<b>w</b> raste s duljinom vektora, a duljina ovisi o učestalosti riječi, pa bi česte riječi bile »slične« svemu. Kosinus cos = <b>v</b>·<b>w</b> / (|<b>v</b>||<b>w</b>|) normira duljine i mjeri samo kut (smjer), tj. sličnost konteksta. Za brojeve ≥ 0 je između 0 i 1.
<b>Česte riječi:</b> najčešći konteksti gotovo svake riječi su zarez, »je«, »i«, »u«. Oni ne govore ništa o riječi, ali imaju najveće brojeve i dominiraju vektorom, pa riječi izgledaju slične samo zato što stoje uz iste česte riječi (»grčka« je po sirovim brojevima najbliža veznicima).
$ PMI(w, c) = log<sub>2</sub> [ P(w, c) / (P(w) P(c)) ],     PPMI(w, c) = max(PMI(w, c), 0)
<b>PMI</b> mjeri pojavljuju li se w i c zajedno češće nego da su neovisni: 0 = kao slučajno, 1 = dvaput češće, negativno = rjeđe. Česti, ali neinformativni konteksti tako dobivaju malu težinu. <b>PPMI</b> negativne vrijednosti (na malom korpusu nepouzdane) postavlja na 0. Slabost: PMI precjenjuje rijetke parove."""),
}

