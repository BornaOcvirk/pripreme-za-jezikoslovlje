r"""Kviz (višestruki izbor) i probni kolokvij.

MCQ: (tema, pitanje, [A, B, C, D], indeks točnog, pomoć kod pogreške, objašnjenje).
"""

MCQ = [
# ---------------- P2 ----------------
("P2 Riječi i tokeni",
 "Rečenica »Na stolu je knjiga, na knjizi je olovka, a na olovki je mrav.« (mala slova, bez interpunkcije). Koliko ima pojavnica N i različnica |V|?",
 ["N = 16, |V| = 9", "N = 13, |V| = 9", "N = 13, |V| = 13", "N = 9, |V| = 13"], 1,
 "Interpunkciju ne brojimo. »na« i »je« pojavljuju se po tri puta.",
 "13 riječi ukupno (pojavnice), a 9 različitih: na, stolu, je, knjiga, knjizi, olovka, a, olovki, mrav. »knjiga« i »knjizi« su dvije različnice. 16 bi bilo s dva zareza i točkom."),
("P2 Riječi i tokeni",
 "Koliko bajtova u UTF-8 zauzima slovo »č« (U+010D)?",
 ["1", "3", "2", "4"], 2,
 "Pogledaj u koji raspon pada U+010D: do U+007F je 1 bajt, do U+07FF 2 bajta …",
 "U+010D je između U+0080 i U+07FF, pa se zapisuje predloškom 110yyyyy 10xxxxxx = C4 8D. Zato »računalno« ima 9 znakova, a 10 bajtova."),
("P2 Riječi i tokeni",
 "Koji je od ovih primjera <b>tvorba</b> (derivacija), a ne fleksija?",
 ["knjiga → knjizi", "čitam → čitaš", "mačka → mačkama", "čitati → čitatelj"], 3,
 "Fleksija daje oblik <i>iste</i> riječi, a tvorba <i>novu</i> riječ.",
 "»čitatelj« je nova riječ (druga vrsta riječi: imenica od glagola). Ostalo su oblici iste riječi (padež, lice, broj), dakle fleksija."),
("P2 Riječi i tokeni",
 "BPE je naučio spajanja ovim redom: n+e, ne+w, ▁+r, ▁r+e, ▁+new, ▁re+new, s+e, se+t. Kako se kodira nova riječ »resets«?",
 ["▁re set s", "▁res ets", "▁r e s e t s", "▁re se ts"], 0,
 "Kreni od ▁ r e s e t s i primijeni spajanja <i>istim redom</i> kojim su naučena.",
 "▁+r → ▁r, ▁r+e → ▁re, s+e → se, se+t → set. Ostaje zadnji »s«: ▁re set s. Frekvencije u novom tekstu nisu važne, važan je samo redoslijed iz učenja."),
("P2 Riječi i tokeni",
 "Koji problem rješava BPE koji kreće od <b>bajtova</b> UTF-8 umjesto od znakova?",
 ["spajanje preko granica riječi", "predugi nizovi tokena", "znakovi kojih nije bilo u korpusu (emoji, druga pisma)", "višeznačnost riječi"], 2,
 "Koliko različitih vrijednosti ima jedan bajt?",
 "Bajt ima samo 256 vrijednosti, pa početni rječnik pokriva svaki mogući tekst: nema nepoznatih tokena. Spajanje preko granica riječi rješava predtokenizacija."),
# ---------------- P3 ----------------
("P3 Regularni izrazi",
 "Što vraća `re.findall(r\"[a-z]+\", \"Računalno\")`?",
 ["['Računalno']", "['a', 'unalno']", "['R', 'ačunalno']", "['unalno']"], 1,
 "Je li »č« između »a« i »z« po kodnim točkama? A »R«?",
 "R je veliko slovo, a č (U+010D) nije u rasponu a–z (U+0061–U+007A), pa se riječ prekida: ['a', 'unalno']. Rješenje: `\\w+` ili `[a-zčćđšž]+`."),
("P3 Regularni izrazi",
 "Tekst je `Rekao je \"da\", pa \"ne\".` Što vraća `re.findall(r'\".*?\"', s)`?",
 ["['\"da\", pa \"ne\"']", "['da', 'ne']", "[]", "['\"da\"', '\"ne\"']"], 3,
 "Upitnik iza zvjezdice čini je <i>nepohlepnom</i>. Što to znači?",
 "`*?` uzima što manje znakova, pa svako podudaranje staje na prvom sljedećem navodniku. Pohlepni `\".*\"` bi uzeo sve od prvog do zadnjeg navodnika."),
("P3 Regularni izrazi",
 "Što nalazi izraz `mačka|ke` u tekstu »mačke mačka«?",
 ["['ke', 'mačka']", "['mačke', 'mačka']", "['mačka']", "['ke', 'ke']"], 0,
 "Niz veže jače od disjunkcije: je li to »mačk(a|e)« ili »(mačka)|(ke)«?",
 "Izraz znači »mačka« ILI »ke«. U riječi »mačke« nema »mačka«, ali ima »ke«. Za mačka/mačke treba `mačk(a|e)`."),
("P3 Regularni izrazi",
 "U »Je li to jezik? Da, to je jezik koji je lijep.« treba naći 3 pojavnice riječi je. Izraz `r\"je\"` pronađe 5 podudaranja, od kojih su 2 točna. Preciznost i odziv?",
 ["P = 2/3, R = 2/5", "P = 3/5, R = 2/3", "P = 2/5, R = 2/3", "P = 2/5, R = 3/3"], 2,
 "Preciznost dijeli s pronađenima, a odziv sa svima koje treba naći.",
 "P = točno pronađeni / svi pronađeni = 2/5 (jezik, jezik, lijep su lažno pozitivni). R = točno pronađeni / svi koje treba = 2/3 (»Je« je lažno negativan)."),
("P3 Regularni izrazi",
 "Što vraća `re.findall(r\"\\d+(?= €)\", \"Kava 2 €, sok 3 €, 5 komada\")`?",
 ["['2', '3', '5']", "['2', '3']", "['2 €', '3 €']", "['5']"], 1,
 "`(?= €)` je pogled unaprijed: provjerava, ali ne troši znakove.",
 "Uzimaju se samo brojevi iza kojih slijedi » €«, a sam » €« nije dio podudaranja. 5 otpada jer iza njega dolazi »komada«."),
# ---------------- P4 ----------------
("P4 Automati i udaljenost",
 "Zašto u tokenizatoru napisanom regularnim izrazom kratice (`dr\\.`) moraju doći <b>prije</b> alternative `\\w+`?",
 ["re uvijek bira najdulju alternativu", "zbog zastavice (?x)", "tako je brže", "re bira prvu alternativu koja uspije, pa bi `\\w+` uzeo »dr« bez točke"], 3,
 "Kako re bira među alternativama A|B|C na istom položaju?",
 "Alternative se isprobavaju slijeva nadesno i pobjeđuje <b>prva</b> koja uspije, a ne najdulja. Zato idu redom: kratice → datumi → brojevi → riječi → interpunkcija."),
("P4 Automati i udaljenost",
 "Automat za ovčji jezik `baa+!` (q0 –b→ q1 –a→ q2 –a→ q3, petlja a na q3, q3 –!→ q4). Koji string <b>prihvaća</b>?",
 ["baaaa!", "ba!", "baa", "bba!"], 0,
 "Mora završiti u prihvatnom stanju q4, a za svaki znak mora postojati prijelaz.",
 "baaaa!: q0 → q1 → q2 → q3 → q3 → q3 → q4. »ba!« zapne u q2 (nema prijelaza za !), »baa« završi u q3 (nije prihvatno), »bba!« zapne već na drugom b."),
("P4 Automati i udaljenost",
 "Koji od ovih jezika <b>nije</b> regularan?",
 ["{baa!, baaa!, baaaa!, …}", "{ab, aabb}", "aⁿbⁿ = {ab, aabb, aaabbb, …}", "svi stringovi od slova a i b"], 2,
 "Što automat s konačno mnogo stanja ne može? (I pazi: je li konačan skup regularan?)",
 "Za aⁿbⁿ automat bi morao brojati a-ove proizvoljno daleko, a ima konačno mnogo stanja. {ab, aabb} je konačan, pa je regularan (svaki konačni jezik je regularan)."),
("P4 Automati i udaljenost",
 "Kolika je Levenshteinova udaljenost (sve operacije koštaju 1) između »pjesma« i »pisma«?",
 ["1", "2", "3", "4"], 1,
 "Probaj: što treba obrisati, a što zamijeniti?",
 "Obriši j, zamijeni e → i: 2 operacije (D[6, 5] = 2). Uz zamjenu = 2 bilo bi 3 (brisanje j + brisanje e + umetanje i)."),
("P4 Automati i udaljenost",
 "Koliko je D[i, 0] u tablici minimalne udaljenosti uređivanja?",
 ["0", "j", "i", "1"], 2,
 "D[i, 0] je udaljenost prvih i znakova izvora od <i>praznog</i> stringa.",
 "Da od i znakova dobiješ prazni string, trebaš i brisanja: D[i, 0] = i. Analogno D[0, j] = j (j umetanja)."),
# ---------------- P5 ----------------
("P5 N-gramski modeli",
 "Korpus: `<s> ja sam Ana </s>`, `<s> Ana ja sam </s>`, `<s> ja ne volim zelena jaja i šunku </s>`. Koliko je P(sam | ja) (MLE)?",
 ["2/3", "1/3", "1/2", "1"], 0,
 "MLE: C(ja sam) / C(ja).",
 "»ja« se pojavljuje 3 puta, a iza njega »sam« dolazi 2 puta: 2/3 ≈ 0,67."),
("P5 N-gramski modeli",
 "Na kojem skupu biramo hiperparametar k kod izglađivanja dodaj-k?",
 ["na skupu za učenje", "na testnom skupu", "svejedno je", "na razvojnom skupu"], 3,
 "Test smijemo gledati samo jednom, na kraju.",
 "k biramo na razvojnom (dev) skupu, tamo gdje je PP najmanja. Testni skup gledamo samo za izabrani k, inače je rezultat precijenjen."),
("P5 N-gramski modeli",
 "Model u jeziku od 4 boje svakoj boji daje vjerojatnost 1/4. Kolika mu je perpleksija na bilo kojem testu?",
 ["1", "4", "0,25", "16"], 1,
 "Perpleksija je težinski faktor grananja: između koliko jednako vjerojatnih riječi model bira?",
 "PP = ((1/4)<super>N</super>)<super>−1/N</super> = 4. Model u svakom koraku »bira« između 4 jednako vjerojatne riječi."),
("P5 N-gramski modeli",
 "Bigramski MLE model, a u testnoj rečenici je jedan bigram kojeg nije bilo u skupu za učenje. Kolika je perpleksija?",
 ["0", "jednaka unigramskoj", "∞", "1"], 2,
 "Kolika je MLE vjerojatnost neviđenog bigrama i što se dogodi s umnoškom?",
 "P(neviđeni bigram) = 0, pa je cijela vjerojatnost 0, a PP = 1/0 = ∞. Lijek je izglađivanje."),
("P5 N-gramski modeli",
 "Zašto je na korpusu SET bigramski model s Laplaceom (PP 1201,5) lošiji od unigramskog (PP 388)?",
 ["Laplace ne uklanja nule", "rječnik je velik, pa dodane jedinice za neviđene bigrame »pojedu« vjerojatnost viđenih", "korpus je prevelik", "zbog oznake `<unk>`"], 1,
 "Što se dogodi s nazivnikom C(w<sub>n−1</sub>) + V kad je V = 30 135?",
 "Nazivnik postane skoro samo V, pa P(je | rekao) padne s 0,71 na 0,0031. Viđeni bigrami izgube previše mase. Bolje: dodaj-k s malim k ili interpolacija."),
# ---------------- P6 ----------------
("P6 Klasifikacija",
 "Težine w = [1,25; 2,04; −1,14], b = −0,62, rečenica ima x = [1, 0, 0]. Što model odluči?",
 ["hrvatski, σ ≈ 0,35", "ne može se odrediti", "SETimes, σ = 0,63", "SETimes, σ ≈ 0,65"], 3,
 "Izračunaj z = w·x + b pa σ(z). Pazi: z i σ(z) nisu isto.",
 "z = 1,25 − 0,62 = 0,63; σ(0,63) ≈ 0,65 &gt; 0,5, pa je odluka SETimes. 0,63 je logit z, a ne vjerojatnost."),
("P6 Klasifikacija",
 "Koliko je σ(0)?",
 ["0,5", "0", "1", "−1"], 0,
 "σ(z) = 1 / (1 + e<super>−z</super>), a e<super>0</super> = 1.",
 "σ(0) = 1/(1 + 1) = 0,5. Rečenica kojoj su sve značajke 0 dobiva P = σ(b), pa o njoj odlučuje samo pomak."),
("P6 Klasifikacija",
 "Jedan korak gradijentnog spusta: x = [1, 0, 0], y = 1, w = [0, 0, 0], b = 0, η = 0,1. Kolike su nove težine?",
 ["[0,1; 0; 0]", "[0,5; 0; 0]", "[0,05; 0; 0]", "[0,05; 0,05; 0,05]"], 2,
 "ŷ = σ(0) = 0,5; gradijent je (ŷ − y)·x<sub>j</sub>.",
 "Gradijent = (0,5 − 1)·[1, 0, 0] = [−0,5, 0, 0]; w = w − 0,1·gradijent = [0,05; 0; 0]. Značajke s x<sub>j</sub> = 0 ne mijenjaju težinu."),
("P6 Klasifikacija",
 "Klasifikator je 50 rečenica pripisao SETimesu, 40 točno; u testu je 80 rečenica iz SETimesa. Koliki je F1?",
 ["0,8", "0,5", "0,65", "0,615"], 3,
 "P = 40/50, R = 40/80, F1 = 2PR/(P + R).",
 "P = 0,8, R = 0,5, F1 = 2·0,8·0,5 / 1,3 ≈ 0,615. Harmonijska sredina je bliža manjoj vrijednosti."),
("P6 Klasifikacija",
 "Klasifikator »uvijek SETimes« ima točnost 56,6 %. Što je problem?",
 ["prenaučen je", "točnost skriva da ne pronalazi nijednu rečenicu hrvatskih izvora", "stopa učenja je prevelika", "nema problema, 56,6 % je dobro"], 1,
 "Što točnost govori o rjeđem razredu?",
 "Kad su razredi neuravnoteženi, točnost nagrađuje stalno pogađanje češćeg razreda. F1 za »hrvatski« je 0, a makro F1 samo 0,361."),
# ---------------- P7 ----------------
("P7 Vektorska semantika",
 "Koliki je kosinus između vektora [1, 0, 2] i [2, 0, 4]?",
 ["0", "1", "0,5", "10"], 1,
 "Drugi vektor je prvi pomnožen s 2. Kakav im je kut?",
 "Isti smjer, različita duljina: kut 0, kosinus 1. Skalarni umnožak (10) ovisi o duljini, a kosinus ne, i zato ga koristimo."),
("P7 Vektorska semantika",
 "P(w, c) = 0,002, a P(w)·P(c) = 0,0005. Koliki je PMI?",
 ["0,25", "4", "2", "−2"], 2,
 "PMI = log<sub>2</sub> omjera. Koliki je omjer?",
 "Omjer = 0,002 / 0,0005 = 4, a log<sub>2</sub> 4 = 2: par se pojavljuje 4 puta češće nego slučajno. Za umnožak 0,004 PMI bi bio −1, a PPMI 0."),
("P7 Vektorska semantika",
 "Koja riječ ima idf = 0?",
 ["najrjeđa riječ u zbirci", "riječ koja se pojavljuje u svim dokumentima", "riječ koja se pojavljuje točno jednom", "nijedna, idf je uvijek pozitivan"], 1,
 "idf = log<sub>10</sub>(N / df). Kada je log jednak 0?",
 "Ako je df = N, idf = log 1 = 0. Takva riječ ne razlikuje dokumente, pa je dobro što je zanemarena (»je« ima idf 0,002)."),
("P7 Vektorska semantika",
 "Zašto word2vec <b>ne</b> predviđa kontekst softmaxom po cijelom rječniku?",
 ["softmax ne daje vjerojatnosti", "rječnik je premalen", "softmax ne može učiti vektore", "nazivnik zbraja po cijelom rječniku za svaki par, a to je preskupo"], 3,
 "Koliko skalarnih umnožaka treba nazivnik softmaxa?",
 "Za svaki par (riječ, kontekst) nazivnik ide po svih |V| riječi. Skip-gram umjesto toga pita binarno »susjed ili ne?« (sigmoid) uz nekoliko nasumičnih protuprimjera."),
("P7 Vektorska semantika",
 "Zašto je fastText posebno koristan za hrvatski?",
 ["vektor riječi je zbroj vektora znakovnih n-grama, pa i rijetki ili nepoznati oblici dobiju dobar vektor", "razlikuje smislove riječi", "ne treba korpus", "koristi tf-idf"], 0,
 "Koliko oblika ima hrvatska imenica i koliko ih se vidi u korpusu?",
 "»utakmica« i »utakmicu« dijele 6 od 8 trigrama, pa su im vektori slični, a i nepoznati oblik dobije vektor iz dijelova. Smislove i dalje ne razlikuje."),
]

PROBNI = [
("Zadatak 1. Riječi, Unicode i BPE (P2)",
 r"""Objasnite kako radi kodiranje <b>UTF-8</b> i zašto »č« zauzima dva bajta. Koju zamku Unicode donosi za hrvatski i kako je rješava <b>normalizacija NFC</b>?""",
 r"""1. Napišite `clean(text)` (samo riječi od slova, malim slovima) i za tekst `"Ana voli jezik. Jezik voli Anu, a Ana voli i jezikoslovlje!"` ispišite N, |V| i tri najčešće riječi.
2. Za riječi »jezik«, »računalno« i »čćđšž« ispišite broj znakova i broj bajtova u UTF-8. Provjerite jesu li `"č"` i `"č"` jednaki prije i nakon normalizacije NFC.
3. Na korpusu `low low lower lowest newest` napravite <b>dva</b> spajanja BPE-a i nakon svakog ispišite par i rastav riječi.""",
 r"""<b>UTF-8</b> zapisuje kodnu točku Unicodea s 1–4 bajta, a početni bitovi kažu koliko ih ima: 0xxxxxxx (do U+007F, ASCII), 110yyyyy 10xxxxxx (do U+07FF), 1110zzzz … (do U+FFFF), 11110uuu … (do U+10FFFF). <b>č = U+010D</b> je u drugom rasponu, pa se njegovih 11 bitova (00100 001101) upiše u 110<b>00100</b> 10<b>001101</b> = <b>C4 8D</b>, tj. dva bajta.
<b>Zamka:</b> č se može zapisati kao jedna kodna točka (U+010D) ili kao c + kombinirajuća kvačica (U+030C). Izgleda isto, ali su stringovi različiti (`==` je False, pretraga ih ne izjednačava). <b>NFC</b> (`unicodedata.normalize("NFC", s)`) sve svodi na jednu kodnu točku, pa se zapisi mogu uspoređivati.""",
 r"""• N = 11, |V| = 7, najčešća je »voli« (3 puta). »Jezik« i »jezik« su ista različnica nakon `.lower()`.
• Hrvatska slova su 2 bajta: »računalno« ima 9 znakova i 10 bajtova, »čćđšž« 5 znakova i 10 bajtova.
• Prije NFC dva zapisa č nisu jednaka, a nakon NFC jesu.
• BPE: (l, o) i (o, w) imaju po 4 pojave (`most_common` uzima prvi prebrojeni), pa nastaje »lo«, a zatim »low«. »newest« ostaje nedirnut jer nema ni »l«."""),
("Zadatak 2. Grupe, pogled unaprijed i tablica D (P3–P4)",
 r"""Što su <b>grupe za hvatanje</b>, <b>povratna referenca</b> i <b>pogled unaprijed</b>? Za svaki pojam navedite primjer u Pythonu.""",
 r"""Tekst: `"Kava je 20 kn, a sok 30 kn. Rekao je je da ne ne dolazi. Cijena: 1.250 kn."`
1. Izdvojite sve iznose ispred » kn«, <b>bez</b> same oznake (i 1.250).
2. Pronađite ponovljene riječi (»je je«).
3. Funkcijom `re.sub` zamijenite svaki »X kn« s »X HRK«.
4. Ispunite tablicu D minimalne udaljenosti za »mak« → »rak« i ispišite D[3, 3]; koliko je uz zamjenu = 2?""",
 r"""• <b>Grupa za hvatanje</b> `( … )` pamti dio podudaranja; u zamjeni ga vraćamo s `\1, \2 …`: `re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\2. \1. \3.", "10/15/2011")` → »15. 10. 2011.«.
• <b>Povratna referenca</b> `\1` <i>unutar</i> uzorka traži isti tekst koji je uhvatila grupa 1: `r"\b(\w+)\s+\1\b"` nalazi ponovljene riječi.
• <b>Pogled unaprijed</b> `(?=X)` provjerava da iza slijedi X, ali X ne ulazi u podudaranje (nulta širina): `r"\d+(?= €)"` vraća iznose bez oznake €. Postoje i `(?!X)`, `(?<=X)`, `(?<!X)`.""",
 r"""• `\d+(?:\.\d{3})*` hvata i točku za tisuće; grupa bez hvatanja `(?:…)` je tu da `findall` vrati cijeli broj, a ne samo grupu.
• Povratna referenca nalazi »je« i »ne«.
• U zamjeni je iznos u grupi 1, a »kn« se zamijeni s »HRK«.
• Tablica: m → r je zamjena (1), a i k se poklapaju (0), pa je D[3, 3] = <b>1</b>; uz zamjenu = 2 je <b>2</b> (obriši m + umetni r)."""),
("Zadatak 3. Izglađivanje i perpleksija (P5)",
 r"""Objasnite izglađivanje <b>dodaj-k</b> i <b>interpolaciju</b>. Kako biramo k i težine λ i zašto ih ne biramo na testnom skupu?""",
 r"""Korpus: `volim jezik`, `volim jezikoslovlje`, `jezik volim` (dodajte `<s>` i `</s>`).
1. Izračunajte MLE P(jezik | volim) i P(volim | `<s>`).
2. Izračunajte perpleksiju rečenica <i>jezik volim jezik</i> i <i>jezikoslovlje volim</i> s MLE-om, s dodaj-k (k = 0,5) i s interpolacijom 0,7 · bigram + 0,3 · unigram. Što primjećujete?""",
 r"""<b>Dodaj-k:</b> P = (C(w<sub>n−1</sub>w<sub>n</sub>) + k) / (C(w<sub>n−1</sub>) + kV), uz k &lt; 1 (Laplace je k = 1). Neviđeni bigrami dobiju malo vjerojatnosti, a viđeni gube manje nego kod Laplacea; svi neviđeni dobivaju jednako.
<b>Interpolacija:</b> P̂ = λ<sub>1</sub>P(w<sub>n</sub>) + λ<sub>2</sub>P(w<sub>n</sub>|w<sub>n−1</sub>) + λ<sub>3</sub>P(w<sub>n</sub>|w<sub>n−2</sub>w<sub>n−1</sub>), uz Σλ = 1: kad duljeg n-grama nema, pomažu kraći.
<b>k i λ su hiperparametri:</b> ne dobivamo ih brojanjem, nego biramo vrijednosti s najmanjom perpleksijom (najvećom vjerojatnošću) na <b>razvojnom</b> skupu. Na testnom skupu ne smijemo, jer bi rezultat bio precijenjen (model bi bio podešen baš za test). Test mjerimo jednom, na kraju.""",
 r"""• P(jezik | volim) = 1/3, P(volim | `<s>`) = 2/3; V = 5 (`<s>`, `</s>`, volim, jezik, jezikoslovlje).
• <i>jezik volim jezik</i>: svi bigrami su viđeni, pa je MLE najbolji (PP 2,449), a izglađivanje malo pogorša PP, jer daje masu i neviđenima.
• <i>jezikoslovlje volim</i>: bigram (jezikoslovlje, volim) nije viđen, pa je MLE = <b>∞</b>, a dodaj-k i interpolacija daju konačnu PP. Upravo zato izglađujemo."""),
("Zadatak 4. Značajke, SGD i makro F1 (P6)",
 r"""Što je <b>matrica zabune</b>? Zašto <b>točnost</b> nije dobra mjera kad razredi nisu uravnoteženi? Definirajte preciznost, odziv, F1 i <b>makro prosjek</b>.""",
 r"""1. S težinama s predavanja (w = [1,25; 2,04; −1,14], b = −0,62) i značajkama »kako« / navodnici / 1. lice klasificirajte rečenice: `Ministar je izjavio kako će "uskoro" doći.`, `Mi smo napokon stigli kući.`, `Kako ste vi?`
2. Napravite jedan korak SGD-a za x = [0, 0, 1], y = 0, w = 0, b = 0, η = 0,5.
3. Za `gold = ["set"]*30 + ["hr"]*20` i `pred = ["set"]*25 + ["hr"]*5 + ["set"]*8 + ["hr"]*12` izračunajte P, R, F1 za oba razreda, točnost i makro F1.""",
 r"""<b>Matrica zabune</b> uspoređuje odluke sustava sa zlatnim oznakama: tp (sustav i zlatna oznaka pozitivni), fp (sustav pozitivan, a nije), fn (pozitivan, a sustav ga je propustio), tn.
<b>Točnost</b> = (tp + tn) / sve. Kod neuravnoteženih razreda visoka je i kad sustav uvijek kaže češći razred (»uvijek SETimes« = 56,6 %, a ne pronalazi nijednu hrvatsku rečenicu), pa ne pokazuje kako sustav radi za rjeđi razred.
P = tp / (tp + fp), R = tp / (tp + fn), F1 = 2PR / (P + R). <b>Makro F1</b> = prosjek F1 po razredima; svaki razred vrijedi jednako, pa slab rjeđi razred snižava rezultat (mikro prosjek zbraja tp, fp, fn preko razreda).""",
 r"""• Prva rečenica ima »kako« i navodnike, pa je P(set) = 0,94. Druga ima dvije riječi 1. lica, pa je 0,05 → hr.
• »Kako ste vi?« dobiva <b>set</b> (0,65) samo zbog riječi »kako«. To je <b>prečac</b>: model ne zna da je ovdje »kako« upitna riječ.
• SGD: ŷ = σ(0) = 0,5, pogreška 0,5; mijenja se samo w<sub>3</sub> = 0 − 0,5·0,5·1 = −0,25 i b = −0,25.
• Točnost je 0,74, ali makro F1 0,721 pokazuje da je razred »hr« slabiji (R = 0,6)."""),
("Zadatak 5. tf-idf i PMI (P7)",
 r"""Definirajte <b>tf</b>, <b>idf</b> i <b>tf-idf</b>. Koja riječ ima idf 0? Koje je ograničenje tf-idf-a za hrvatski i kako ga ublažavaju LSA ili fastText?""",
 r"""Dokumenti: `utakmica je završila neriješeno` · `trener je nakon utakmice zadovoljan` · `cijena kruha je porasla` · `kuna je jača nego prošle godine i cijena je viša`
1. Izračunajte matricu tf-idf formulama s predavanja (log<sub>10</sub>) i ispišite idf za »je«, »cijena« i »utakmica«.
2. Izračunajte kosinus upita »utakmica« sa svakim dokumentom. Zašto drugi dokument (o treneru) dobiva 0?
3. Izračunajte PMI ako je N = 1000 parova, broj(w) = 20, broj(c) = 50 i broj(w, c) = 5.""",
 r"""tf(t, d) = log<sub>10</sub>(broj(t, d) + 1) prigušuje velike brojeve; idf(t) = log<sub>10</sub>(N / df(t)) daje veću težinu riječima rijetkima u zbirci; tf-idf = tf · idf je velik za riječi česte u dokumentu, a rijetke u zbirci.
<b>idf = 0</b> ima riječ koja je u svim dokumentima (N/df = 1), jer ne razlikuje dokumente.
<b>Ograničenje:</b> tf-idf uspoređuje točne oblike, a hrvatski ima mnogo oblika: »utakmica« i »utakmicu« su za njega nepovezane riječi. <b>LSA</b> spaja riječi koje se pojavljuju u istim dokumentima u teme, pa povezuje i dokumente bez zajedničke riječi. <b>fastText</b> gradi vektor riječi od znakovnih n-grama, pa su oblici iste riječi slični.""",
 r"""• »je« je u sva 4 dokumenta, pa je idf = log 1 = <b>0</b>; »cijena« je u 2 (idf = log 2 = 0,301); »utakmica« u 1 (idf = log 4 = 0,602).
• Upit je sličan samo prvom dokumentu (0,577). Drugi ima »utakmice«, a za tf-idf je to <b>druga riječ</b>, pa je kosinus 0. To je ograničenje za hrvatski.
• PMI = log<sub>2</sub>(5 · 1000 / (20 · 50)) = log<sub>2</sub> 5 ≈ <b>2,32</b>: par je 5 puta češći nego slučajno."""),
]
