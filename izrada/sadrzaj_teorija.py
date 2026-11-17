r"""Odgovori na teorijska pitanja iz kolokvij_1_pitanja.docx (P2–P7).

Oznake: prazan red = novi odlomak; "• " = natuknica; "$ " = formula; "| a | b |" = redak tablice
(prvi redak je zaglavlje); ``` ... ``` = blok koda; `x` = kod u retku; [[q3_5|tekst]] = poveznica.
Izvan `...` znakove < i > pišemo kao &lt; i &gt;.
"""

GITHUB = "https://github.com/dseverdi/CL/tree/main"
GITHUB_KOL = "https://github.com/dseverdi/CL/tree/main/kolokvij"

TOPICS = [
# =====================================================================================
("t1", "1. Riječi i tokeni (P2)", "teorija_p2_unicode_bpe.py", [
("q1_1", "Riječi u tekstu: različnice, pojavnice, Heapsov zakon",
 r"""Riječi u tekstu: definirajte različnicu i pojavnicu te ih odredite za rečenicu po izboru. Iskažite Heapsov zakon i objasnite što govori o nepoznatim riječima i zašto rječnik hrvatskog raste brže od engleskog. Koje odluke treba donijeti pri brojanju riječi (velika i mala slova, »neću«, višečlani izrazi, jezici bez razmaka)?""",
 r"""<b>Pojavnica</b> (engl. <i>word instance</i>) je svako pojavljivanje riječi u tekstu; njihov broj označavamo s <b>N</b>. <b>Različnica</b> (engl. <i>word type</i>) je svaka različita riječ; skup različnica je <b>rječnik V</b>, a njihov broj |V|. Naziv <i>token</i> čuvamo za jedinice koje daje tokenizator.

<b>Primjer</b> (P2, sl. 6): »Na stolu je knjiga, na knjizi je olovka, a na olovki je mrav.«
• Bez interpunkcije i malim slovima: <b>N = 13</b> pojavnica, <b>|V| = 9</b> različnica (na, stolu, je, knjiga, knjizi, olovka, a, olovki, mrav).
• »na« i »je« pojavljuju se po 3 puta. <i>knjiga</i> i <i>knjizi</i> su dvije različnice, iako su ista riječ u rječniku (dva oblika iste leme).
• S interpunkcijom (2 zareza i točka kao zasebne jedinice) ima 16 jedinica.

<b>Heapsov (Herdanov) zakon</b> povezuje veličinu rječnika s duljinom teksta:
$ |V| = k · N<super>β</super>,   k, β &gt; 0,   0 &lt; β &lt; 1
Na engleskim korpusima β ≈ 0,44–0,56, pa rječnik raste malo brže od drugog korijena duljine teksta. Najvažnije: <b>rječnik ne prestaje rasti</b>. Funkcijskih riječi (i, u, je) ima konačno mnogo, a sadržajne riječi (imena, nazivi, novi pojmovi) stalno pristižu. Zato će u svakom novom tekstu biti <b>nepoznatih riječi</b> (OOV), i model se mora znati nositi s njima (podriječi, oznaka `<unk>`).

<b>Zašto hrvatski raste brže:</b> hrvatski ima bogatu fleksiju (7 padeža, rod, broj, glagolski oblici). Jedna lema ima mnogo oblika (knjiga, knjige, knjizi, knjigu, knjigom …), a svaki oblik je zasebna različnica. U korpusu SET oblika je gotovo dvaput više nego lema. Uz isti broj pojavnica N hrvatski zato ima veći |V| od engleskog.

<b>Odluke pri brojanju riječi</b> (sve »ovise o zadatku«):
| Pitanje | Primjer | Odluka |
| velika i mala slova? | Na / na | izjednačiti za brojanje; zadržati kad slova nose informaciju (imena, NER) |
| jedna ili dvije riječi? | neću = ne + ću | pravopisno jedna, gramatički dvije (kao engl. I'm) |
| višečlani izrazi? | Republika Hrvatska, New York | ponekad jedan token (imenovani entiteti) |
| interpunkcija? | zarez, točka | zasebna jedinica ili se izostavlja |
| govorni jezik? | »ovaj«, »hm«, »uglav-« | ispune i fragmenti: brojati ako pomažu (npr. prepoznavanje govora) |
| jezici bez razmaka | kineski, japanski, tajlandski | potrebna segmentacija riječi |
Kod jezika bez razmaka, kineska rečenica »Yao Ming ulazi u finale« (7 znakova) ima 3 riječi po standardu Chinese Treebanka (ime je jedna riječ), 5 riječi po standardu Sveučilišta u Pekingu ili 7 jedinica ako je svaki znak jedinica."""),

("q1_2", "Morfologija: morfem, korijen, afiks, fleksija, tvorba, klitike, tipologija",
 r"""Morfologija: što je morfem, a što korijen i afiks? Objasnite razliku između fleksije i tvorbe na hrvatskim primjerima te što su klitike. Opišite morfološku tipologiju (analitički, sintetički, polisintetički jezici; aglutinacija i fuzija) i smjestite hrvatski u nju.""",
 r"""<b>Morfem</b> je najmanja jedinica jezika koja ima značenje; morfologija proučava morfeme. <b>Korijen</b> nosi glavno značenje riječi (knjig-a, čita-ti, pjev-ač). <b>Afiks</b> je morfem koji se dodaje korijenu: prefiks ispred (<b>ne</b>-ovis-nost), sufiks ili nastavak iza (mačk-<b>ama</b>).
• mačk-a: korijen + nastavak (jednina, nominativ)
• mačk-ama: korijen + nastavak (množina, dativ/lokativ/instrumental)
• uči-telj-ica: korijen + tvorbeni nastavak + tvorbeni nastavak (ženski rod)
• ne-ovis-nost: prefiks + korijen + sufiks

| | Fleksija (pregibanje) | Tvorba (derivacija) |
| što radi | oblici <b>iste</b> riječi; gramatička obilježja (padež, broj, lice …) | <b>nova</b> riječ, često druga vrsta riječi |
| predvidljivost | predvidljiva i obvezna | značenje manje predvidljivo |
| primjeri | knjig-a, knjig-e, knjiz-i; čita-m, čita-š, čita-mo | čita-ti → čita-telj → čitatelj-ica; pjeva-ti → pjev-ač |

<b>Klitika</b> se ponaša kao riječ, ali ne može stajati sama, nego se naslanja na drugu riječ. Hrvatski: enklitike »Dao <b>sam mu ga</b>.«, upitna čestica »Dolaziš <b>li</b>?«; engleski: I<b>'ve</b>, the teacher<b>'s</b> book; francuski: <b>l'</b>opéra, <b>j'</b>ai. Za tokenizaciju klitike su problem: »neću«, »reći ću«, »vidio sam ga«.

<b>Morfološka tipologija</b> (Greenberg 1960.; prosječan broj morfema po riječi):
| tip | obilježje | primjeri (morfema/riječi) |
| analitički (izolacijski) | riječ ≈ jedan morfem; gramatika redoslijedom i pomoćnim riječima | vijetnamski 1,1; perzijski 1,5; engleski 1,7 |
| sintetički | riječ = korijen + više gramatičkih morfema | sanskrt 2,6; <b>hrvatski 2,7</b>; svahili 2,5 |
| polisintetički | cijela »rečenica« u jednoj riječi | grenlandski 3,7 |
Unutar sintetičkih jezika razlikujemo:
• <b>aglutinaciju</b>: morfemi imaju jasne granice, jedan nastavak = jedno značenje (turski <i>ev-ler-iniz-den</i> = kuća + množina + vaš + iz → »iz vaših kuća«);
• <b>fuziju</b>: jedan nastavak stapa više značenja (hrvatski <i>stol-om</i> = instrumental + jednina + muški rod; ruski).
To su tendencije, a ne čista svojstva: i engleski <i>-s</i> u »She read<b>s</b>« stapa 3. lice, jedninu i prezent.

<b>Hrvatski</b> je <b>sintetički, fuzijski (flektivni)</b> jezik: jedna riječ nosi korijen i nekoliko gramatičkih obilježja stopljenih u jedan nastavak. Zato ima mnogo oblika riječi i brže rastući rječnik (veza s [[q1_1|Heapsovim zakonom]])."""),

("q1_3", "Znakovi: ASCII, Unicode, UTF-8, normalizacija",
 r"""Znakovi: objasnite ASCII, Unicode i razliku između kodne točke i glifa. Kako radi kodiranje UTF-8 i zašto znak »č« zauzima dva bajta? Koje zamke Unicode donosi za hrvatski i kako ih rješava normalizacija?""",
 r"""<b>ASCII</b> (1960-e) je kodiranje u kojem je svaki znak jedan bajt. Koristi samo 128 od 256 mogućih vrijednosti (A = 0x41 = 65, a = 0x61 = 97). Hrvatska slova č, ć, đ, š, ž nisu u ASCII-ju, pa su nekad postojala kodiranja Latin-2 (ISO 8859-2) i Windows-1250, a na webu »ošišana« latinica (csdz).

<b>Unicode</b> je standard koji svakom znaku svih pisama dodjeljuje <b>kodnu točku</b>: jedinstven broj, zapisan heksadecimalno s prefiksom U+. Unicode 16.0 ima više od 150 000 znakova i 168 pisama, a prvih 128 kodnih točaka jednako je ASCII-ju. Primjeri: a = U+0061, č = U+010D, ć = U+0107, đ = U+0111, š = U+0161, ž = U+017E.

<b>Kodna točka nije glif.</b> Kodna točka je apstraktni znak (broj), a <b>glif</b> je izgled znaka u nekom fontu. Slovo »a« u fontovima Times New Roman, Courier, podebljano ili kurzivom je pet različitih glifova, ali uvijek ista kodna točka U+0061.

<b>UTF-8</b> je kodiranje promjenjive duljine: kodnu točku zapisuje s 1–4 bajta. Početni bitovi prvog bajta govore koliko bajtova ima znak, a nastavni bajtovi počinju s 10:
| raspon kodnih točaka | bajt 1 | bajt 2 | bajt 3 | bajt 4 |
| U+0000 – U+007F | 0xxxxxxx | | | |
| U+0080 – U+07FF | 110yyyyy | 10xxxxxx | | |
| U+0800 – U+FFFF | 1110zzzz | 10yyyyyy | 10xxxxxx | |
| U+10000 – U+10FFFF | 11110uuu | 10uuzzzz | 10yyyyyy | 10xxxxxx |
ASCII = 1 bajt (pa je UTF-8 kompatibilan s ASCII-jem); hrvatska, grčka i arapska slova = 2 bajta; kineski = 3; emojiji = 4.

<b>Zašto č zauzima dva bajta:</b> kodna točka U+010D veća je od U+007F, a manja od U+07FF, pa pada u drugi redak tablice. Njezinih 11 bitova (0x10D = 00100 001101) rasporedimo u predložak 110yyyyy 10xxxxxx:
$ 110<b>00100</b> 10<b>001101</b> = C4 8D
U Pythonu: `"č".encode("utf-8")` → `b"\xc4\x8d"`. Zato »računalno« ima 9 znakova, ali 10 bajtova.

<b>Zamke za hrvatski:</b>
• <b>č se može zapisati na dva načina:</b> kao jedna kodna točka (U+010D) ili kao dvije: c + kombinirajuća kvačica (U+030C). Izgleda isto, ali su to različiti stringovi: `==` vraća False, `len` se razlikuje, a pretraga i brojanje riječi ne prepoznaju ih kao isto.
• <b>lj, nj, dž</b> su jedno slovo abecede, ali dvije kodne točke (`len("lj") == 2`).
• Datoteka uvijek ima kodiranje: `open(path, encoding="utf-8")`. Pogrešno kodiranje daje »ÄŤ« umjesto »č« (bajtovi C4 8D pročitani kao Windows-1250).
• U Pythonu 3 string je niz kodnih točaka, pa `len()` broji znakove (kodne točke), ne bajtove.

<b>Normalizacija</b> svodi tekst na jedan kanonski zapis. <b>NFC</b> spaja znak i kvačicu u jednu kodnu točku (č = U+010D), a NFD ih rastavlja. Prije usporedbe ili brojanja: `unicodedata.normalize("NFC", s)`."""),

("q1_4", "Tokenizacija BPE: podriječi, učenje, kodiranje, bajtovi, predtokenizacija",
 r"""Tokenizacija BPE: koje su prednosti i nedostaci riječi, morfema i znakova kao jedinica za model i zašto se koriste podriječi? Opišite učenje i kodiranje algoritmom BPE te objasnite koji problem rješava BPE nad bajtovima, a koji predtokenizacija.""",
 r"""| jedinica | prednosti | nedostaci |
| riječi | dobra razina značenja | teško ih je definirati; ima ih previše (Heaps); nepoznate riječi |
| morfemi | dobra razina značenja | teško ih je definirati i automatski rastaviti |
| znakovi | jasno definirani; nema nepoznatih | premala jedinica (malo značenja); predugi nizovi |
<b>Podriječi</b> su kompromis naučen iz podataka. Uglavnom su veličine morfema ili riječi, a po potrebi i pojedini znakovi. Česte riječi postaju jedan token, a rijetke se rastave na dijelove. Svaka nova riječ ima zapis (u najgorem slučaju slovo po slovo), pa <b>nema nepoznatih riječi</b>: <i>stariji</i> → <i>star iji</i>, iako riječ nije bila u skupu za učenje. Tokenizacija usto standardizira tekst, pa se različiti sustavi mogu složiti koliko je tekst dugačak.

<b>BPE ima dva dijela:</b> učenje (iz korpusa inducira rječnik tokena) i kodiranje (novu rečenicu rastavlja na naučene tokene).

<b>Učenje</b> (Sennrich i sur. 2016.; SLP3 sl. 2.6):
```
funkcija BPE(korpus C, broj spajanja k) vraća rječnik V
    V ← svi različiti znakovi u C
    ponovi k puta
        tL, tR ← najčešći par susjednih tokena u C
        tnovi ← tL + tR
        V ← V ∪ {tnovi}
        zamijeni svaki par tL, tR u C s tnovi
    vrati V
```
• Primjer: A B D C A B E C A B → (A+B) → AB D C AB E C AB → (C+AB) → AB D CAB E CAB.
• Spajanja ne prelaze granice riječi; ▁ označava razmak ispred riječi. Na korpusu »set new new renew reset renew« redom se spajaju n+e (4 pojave), ne+w (4), ▁+r (3), ▁r+e, ▁+new, ▁re+new, s+e, se+t.
• Rječnik samo raste: početni znakovi + k novih tokena (7 + 8 = 15). Nijedan token se ne briše.

<b>Kodiranje:</b> novu riječ rastavimo na znakove i primijenimo naučena spajanja <b>istim redoslijedom kojim su naučena</b>. Frekvencije u novom tekstu nisu važne. Primjeri: ▁resets → ▁re set s; newer → ▁new e r; anew → ▁ a new.

<b>BPE nad bajtovima</b> rješava problem <b>nepoznatih znakova</b>. Ako je početni rječnik skup znakova iz korpusa za učenje, znak kojeg tamo nije bilo (rijetko slovo, emoji, drugo pismo) u novom tekstu nema zapis. Kad BPE kreće od bajtova UTF-8, početni rječnik ima samo 256 simbola i svaki tekst ima zapis. BPE zatim prvim spajanjima »ponovno otkrije« hrvatska slova (C4 + 8D = č, kao 15. spajanje).

<b>Predtokenizacija</b> rješava problem <b>spajanja preko granica riječi, brojeva i interpunkcije</b>. To je grubi prvi korak: tekst se pravilima (regularnim izrazima) podijeli na predtokene (riječ s razmakom ispred, broj, interpunkcija), a BPE zatim spaja samo unutar predtokena. »Imamo 350 pasa! Hm, ručak?« → Imamo ·350 ·pasa ! ·Hm , ·ručak ?. Tako »pasa!« nikad ne postane jedan token. U GPT-4o brojevi idu u skupinama do tri znamenke, a klitike poput <i>'s</i> zasebno."""),

("q1_5", "Korpusi: višejezični tokenizatori i podatkovna kartica",
 r"""Korpusi: kakve posljedice za hrvatski ima to što su višejezični tokenizatori učeni pretežno na engleskom? Što je podatkovna kartica korpusa, zašto je potrebna i koje podatke o korpusu (varijetet, žanr, autori, vrijeme) treba opisati?""",
 r"""<b>Višejezični tokenizatori i hrvatski.</b> Korpusi za učenje tokenizatora pretežno su engleski, pa je većina spajanja i tokena »potrošena« na engleske riječi. Ostali jezici se zato pretjerano usitnjavaju: engleski treba prosječno <b>1,50</b> tokena po riječi, a hrvatski <b>2,71</b>. Primjer s predavanja: engleska rečenica od 8 riječi ima 12 tokena, a hrvatska od 7 riječi čak 28 (»Ra č unal no ·j ez ik oslov l je …«). Posljedice (Rust i sur. 2021.; Ahia i sur. 2023.):
• <b>lošije reprezentacije značenja</b>: tokeni nisu morfemi ni riječi, nego proizvoljni komadići;
• <b>dulji nizovi</b>: isti tekst troši više konteksta modela, pa manje teksta stane u kontekst;
• <b>skuplje i sporije</b> treniranje i korištenje (usluge se plaćaju po tokenu), a često i lošiji rezultati.

<b>Tekst ne nastaje niotkuda</b>, nego ga je netko, kada i zašto napisao. Model nauči jezik korpusa, ne »jezik općenito«, pa moramo znati što je u korpusu.

<b>Podatkovna kartica</b> (engl. <i>datasheet</i>; Gebru i sur. 2020.) je dokument koji uz korpus opisuje kako je korpus nastao. Potrebna je da korisnik zna za što je korpus prikladan, koje pristranosti nosi, može li se rezultat poopćiti te kako se korpus smije koristiti i dijeliti. Opisuje:
• <b>motivaciju</b>: tko je i zašto napravio korpus;
• <b>jezik i varijetet</b>: standard, narječja (štokavsko, kajkavsko, čakavsko), regionalni i društveni govori, miješanje jezika (»Imamo meeting u tri …«);
• <b>žanr i situaciju</b>: vijesti, književnost, znanstveni radovi, zakoni, forumi, transkripti razgovora;
• <b>autore</b>: dob, spol, obrazovanje, društveni sloj;
• <b>vrijeme</b>: »Zlatarovo zlato« (1871.) i današnji portali nisu isti jezik;
• <b>prikupljanje i označavanje</b>: koliko teksta, kako je odabran i podijeljen, kakve oznake ima;
• <b>distribuciju</b>: licenciju.

Primjer, UD Croatian SET (korpus s vježbi): hrvatski treebank projekta Universal Dependencies (temelj je korpus hr500k); vijesti SETimes, hrvatski portali i web-tekstovi; standardni hrvatski; demografija autora nije navedena; oko 9000 rečenica s podjelom na učenje i test; leme, vrste riječi, morfologija i zavisnosti; licencija CC BY-SA 4.0."""),
]),
# =====================================================================================
("t2", "2. Regularni izrazi (P3)", "teorija_p3_regex.py", [
("q2_1", "Osnovni pojmovi: string, uzorak, podudaranje, sirovi string, modul re",
 r"""Definirajte pojmove string, uzorak, podudaranje i regularni izraz. Što su sirovi string i metaznak i zašto regularne izraze u Pythonu pišemo kao r"…"? Čemu služe funkcije re.search, re.findall, re.sub i re.split?""",
 r"""• <b>String</b>: konačan niz znakova. Duljina |s| je broj znakova, a prazni string ε ima duljinu 0. <b>Podstring</b> je niz uzastopnih znakova unutar stringa (»uć« je podstring od »kuća«, a »ka« nije).
• <b>Uzorak</b> (engl. <i>pattern</i>): opis stringova koje tražimo u tekstu.
• <b>Podudaranje</b> (engl. <i>match</i>): podstring teksta koji odgovara uzorku. Određeno je položajem: `re.search(r"Zagreb", "Grad Zagreb je glavni grad.")` daje podudaranje na položaju (5, 11).
• <b>Regularni izraz</b>: formalni zapis <b>skupa stringova</b>; string pripada skupu ako se podudara s izrazom. `r"Zagreb"` opisuje {Zagreb}, `r"[zZ]agreb"` opisuje {zagreb, Zagreb}, a `r"baa+!"` beskonačan skup {baa!, baaa!, …}. Služe za pretraživanje, zamjenu, tokenizaciju i provjeru oblika (poštanski broj).

<b>Metaznak</b> je znak s posebnim značenjem u regularnom izrazu: `. ^ $ * + ? { } [ ] \ | ( )`. <b>Izbjegavanje</b> (engl. <i>escaping</i>): obrnuta kosa crta ispred metaznaka vraća mu doslovno značenje (`\.` je točka, `\?` upitnik, `\\` obrnuta kosa crta).

<b>Sirovi string</b> `r"…"` je string u kojem Python ne tumači obrnutu kosu crtu, nego je ona ostaje u stringu i stiže do modula re. To je važno jer u običnom stringu Python sam pretvara `"\t"` u tabulator, a `"\b"` u znak backspace, pa bi re dobio pogrešan uzorak (`\b` u regexu znači granicu riječi). Bez r bismo morali pisati `"\\b"` i `"\\d"`. Pravilo: uzorke uvijek pišemo kao sirove stringove.

| funkcija | što vraća |
| `re.search(uzorak, tekst)` | prvo podudaranje (objekt Match: `.group()`, `.span()`) ili None |
| `re.findall(uzorak, tekst)` | listu svih podudaranja (ako uzorak ima grupe, sadržaj grupa!) |
| `re.sub(uzorak, zamjena, tekst)` | tekst u kojem su sva podudaranja zamijenjena |
| `re.split(uzorak, tekst)` | listu dijelova teksta između podudaranja (npr. segmentacija rečenica) |"""),

("q2_2", "Disjunkcija znakova, raspon, negacija, klase \\d \\w \\s",
 r"""Objasnite disjunkciju znakova, raspon i negaciju te klase znakova \d, \w i \s. Zašto raspon [a-z] ne obuhvaća slovo »č«?""",
 r"""• <b>Disjunkcija znakova</b> `[abc]` podudara se s <b>točno jednim</b> znakom: a, b ili c. Primjeri: `r"[mM]arija"` (Marija ili marija), `r"[čć]"`, `r"[0123456789]"`.
• <b>Raspon</b> `[a-z]` kraći je zapis za sve znakove od a do z <b>po poretku kodnih točaka</b> Unicodea: `[A-Z]` veliko slovo, `[0-9]` znamenka.
• <b>Negacija</b> `[^abc]` podudara se s jednim znakom koji nije a, b ni c. Kapica mora biti prva u zagradi: `[^A-Z]` je bilo što osim velikog slova, a `[e^]` je e ili ^. Unutar `[ ]` većina metaznakova gubi posebno značenje (`[.]` je obična točka).

| kratica | isto što i | značenje |
| `\d` | `[0-9]` | znamenka |
| `\w` | slova, znamenke, _ | riječni znak (u Pythonu 3 uključuje i č, ć, đ, š, ž) |
| `\s` | razmak, `\t`, `\n` … | praznina (engl. <i>whitespace</i>) |
| `\D \W \S` | `[^0-9]` … | negacije prethodnih klasa |

<b>Zašto [a-z] ne obuhvaća č:</b> raspon ide po kodnim točkama. a = U+0061 i z = U+007A, a č = U+010D je izvan tog intervala (kao i ć, đ, š, ž). Zato `re.findall(r"[a-z]+", "Računalno")` vraća `['a', 'unalno']`, jer se riječ prekida na č. Rješenje je `[a-zčćđšž]` ili kratica `\w`: `re.findall(r"\w+", "Računalno jezikoslovlje, 2027.")` vraća `['Računalno', 'jezikoslovlje', '2027']`."""),

("q2_3", "Kvantifikatori, zamjenski znak, sidra, pohlepno i nepohlepno",
 r"""Objasnite kvantifikatore ?, *, +, {n} i {n,m}, zamjenski znak ».« i sidra ^, $ i \b. Koja je razlika između pohlepnog i nepohlepnog podudaranja?""",
 r"""<b>Kvantifikator</b> je operator iza znaka ili izraza koji određuje koliko se puta on ponavlja:
| operator | značenje | primjer | podudara se s |
| `?` | 0 ili 1 put (neobavezno) | `r"Zagrebu?"` | Zagreb, Zagrebu |
| `*` | 0 ili više puta (Kleeneova zvjezdica) | `r"ba*!"` | b!, ba!, baa! … |
| `+` | 1 ili više puta (Kleeneov plus) | `r"baa+!"` | baa!, baaa! … (»ovčji jezik«) |
| `{n}` | točno n puta | `r"[0-9]{5}"` | 31000 |
| `{n,m}` | od n do m puta | `r"[0-9]{1,2}\."` | 5., 15. |

<b>Zamjenski znak</b> `.` podudara se s <b>bilo kojim jednim znakom osim novog retka</b>: `r"r.ka"` nalazi »ruka« i »rika«, ali ne »rijeka«. `.*` je bilo koji niz znakova, uključujući prazni.

<b>Sidra</b> se podudaraju s <b>položajem</b>, a ne sa znakom (»troše« prazni string):
• `^` početak retka: `re.findall(r"^Dr\.", "Dr. Horvat kasni.")` → ['Dr.'];
• `$` kraj retka: `r"kasni\.$"` → ['kasni.'];
• `\b` granica riječi, tj. mjesto između riječnog i neriječnog znaka (ili početka/kraja teksta): `r"\bje\b"` nalazi »je«, ali ne »jezik«. `\B` znači »nije granica riječi«.
Kapica ima tri uloge: početak retka, negacija u `[^ ]` i obični znak ^.

<b>Pohlepno</b> (engl. <i>greedy</i>, zadano ponašanje): kvantifikator uzima <b>što više</b> znakova može. <b>Nepohlepno</b> (`*?`, `+?`, `??`): uzima <b>što manje</b>.
```
s = 'Rekao je "da", pa "ne".'
re.findall(r'".*"', s)    # ['"da", pa "ne"']   od prvog do zadnjeg navodnika
re.findall(r'".*?"', s)   # ['"da"', '"ne"']    do prvog sljedećeg navodnika
re.findall(r"a.*a", "banana")    # ['anana']
re.findall(r"a.*?a", "banana")   # ['ana']
```"""),

("q2_4", "Disjunkcija |, grupiranje, prednost operatora, preciznost i odziv",
 r"""Objasnite disjunkciju | i grupiranje te kako prednost operatora određuje značenje izraza je* i mačka|ke. Kako mjerimo pogreške regularnog izraza preciznošću i odzivom (lažno pozitivni i lažno negativni primjeri)?""",
 r"""<b>Disjunkcija</b> `A|B` podudara se s izrazom A ili s izrazom B, i to s <b>cijelim izrazima</b>, a ne samo sa znakom: `re.findall(r"mačka|pas", "mačka i pas")` → ['mačka', 'pas']. (`[mačkapas]` bi bio samo jedan znak iz skupa.)

<b>Grupiranje</b> `( )`: izraz u zagradama ponaša se kao jedna jedinica za okolne operatore. `r"mač(ka|ke|ku)"` nalazi mačka/mačke/mačku. `ha+` ponavlja samo a (ha, haaa), a `(ha)+` ponavlja cijelu skupinu (hahaha).

<b>Prednost operatora</b> (od najjače): 1. zagrade `( )`; 2. kvantifikatori `* + ? { }`; 3. nizovi i sidra; 4. disjunkcija `|`.
• `je*`: zvjezdica veže jače od niza, pa ponavlja <b>samo e</b>, a ne cijelo »je«. Podudara se s j, je, jee …: `re.findall(r"je*", "j je jee jeje")` → ['j', 'je', 'jee', 'je', 'je']. Za ponavljanje cijelog »je« treba `(je)*`.
• `mačka|ke`: niz veže jače od |, pa izraz znači »mačka« <b>ili</b> »ke«, a ne `mačk(a|e)`. `re.findall(r"mačka|ke", "mačke mačka")` → ['ke', 'mačka']; u riječi »mačke« nađe se samo »ke«.

<b>Pogreške.</b> Tražimo riječ »je« u »Je li to jezik? Da, to je jezik koji je lijep.« (treba naći 3 pojavnice).
• <b>Lažno pozitivan</b> (engl. <i>false positive</i>): pronađen, a ne treba (»je« u <i>jezik</i>, <i>lijep</i>).
• <b>Lažno negativan</b> (engl. <i>false negative</i>): treba, a nije pronađen (»Je« s velikim slovom kod `r"je"`).
$ preciznost = točno pronađeni / svi pronađeni        odziv = točno pronađeni / svi koje treba naći
| izraz | pronađeno | točno | lažno poz. | lažno neg. | preciznost | odziv |
| `r"je"` | 5 | 2 | 3 | 1 | 2/5 | 2/3 |
| `r"[jJ]e"` | 6 | 3 | 3 | 0 | 3/6 | 3/3 |
| `r"\b[jJ]e\b"` | 3 | 3 | 0 | 0 | 3/3 | 3/3 |
Lažno pozitivni smanjuju preciznost (izraz je preširok), a lažno negativni smanjuju odziv (izraz je preuzak). Popravljanje jednog često kvari drugo."""),

("q2_5", "Grupe za hvatanje, povratna referenca, pogled unaprijed/unatrag, ELIZA",
 r"""Što su grupe za hvatanje i kako se koriste u zamjeni? Objasnite povratnu referencu, grupu bez hvatanja te pogled unaprijed i unatrag. Kako radi ELIZA kao kaskada zamjena i zašto za hrvatski treba više pravila nego za engleski?""",
 r"""<b>Grupa za hvatanje</b> (engl. <i>capture group</i>) je dio uzorka u zagradama čije se podudaranje <b>pamti</b>. Grupe se numeriraju slijeva: 1, 2, 3 … i dohvaćaju s `m.group(1)`. U zamjeni `\1, \2, \3` umeću sadržaj grupa, pa možemo preslagati dijelove:
```
re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\2. \1. \3.", "Datum je 10/15/2011")
# 'Datum je 15. 10. 2011.'
re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3. \2. \1.", "2026-10-15")   # '15. 10. 2026.'
```
• <b>Povratna referenca</b> `\1` <b>unutar uzorka</b> podudara se s <b>istim tekstom</b> koji je uhvatila grupa 1: `re.findall(r"\b(\w+)\s+\1\b", "Rekao je je da dolazi.")` → ['je'] (ponovljena riječ).
• <b>Grupa bez hvatanja</b> `(?:…)` samo grupira i ništa ne pamti. Važno je kod `findall`, koji vraća sadržaj grupa: `re.findall(r"(ha)+", "hahaha")` → ['ha'], a `r"(?:ha)+"` → ['hahaha'].
• <b>Pogled unaprijed i unatrag</b> su tvrdnje nulte širine: provjeravaju uvjet na trenutnom položaju, ali ne troše znakove (kao sidra). `(?=X)` znači da slijedi X, `(?!X)` da ne slijedi X, `(?&lt;=X)` da prethodi X, a `(?&lt;!X)` da ne prethodi X. Primjer: `re.findall(r"\d+(?= €)", "Kava 2 €, sok 3 €, 5 komada")` → ['2', '3'] (iznosi bez same oznake €).

<b>ELIZA</b> (Weizenbaum 1966.) oponaša psihoterapeuta koji korisnikove riječi vraća kao pitanje. Radi kao <b>kaskada zamjena</b>: niz `re.sub` koraka u kojem svaki radi na izlazu prethodnog.
1. velika slova: JA SAM TUŽNA VEĆINU VREMENA.
2. zamjenice: JA SAM → TI SI, MOJ → TVOJ: TI SI TUŽNA VEĆINU VREMENA.
3. pravilo uzorak → odgovor, gdje `\1` prenosi dio unosa: `.*TI SI (TUŽAN|TUŽNA).*` → ŽAO MI JE ŠTO SI \1.
4. ako ništa ne odgovara, opći odgovor: »RECI MI NEŠTO VIŠE.«

<b>Zašto hrvatski treba više pravila:</b> engleski je analitičan, pa jedno pravilo »I am X« → »you are X« pokriva sve. Hrvatski traži <b>slaganje</b> u rodu, broju, licu i padežu (tužan/tužna, si/ste, sam/smo), zamjenice se sklanjaju (moj, mojoj, mojem, moga → tvoj, tvojoj, tvojem, tvoga), glagolski oblici se mijenjaju po licu, a enklitike i slobodan red riječi dodaju još varijanti. Svaki oblik traži svoje pravilo: to je posljedica <b>morfologije</b>."""),
]),
# =====================================================================================
("t3", "3. Pravila, automati i udaljenost uređivanja (P4)", "teorija_p4_automati_udaljenost.py", [
("q3_1", "Tokenizacija pravilima, Penn Treebank, redoslijed alternativa",
 r"""Tokenizacija pravilima: po čemu se razlikuje od BPE-a i kada je bolji izbor? Što je banka stabala i standard Penn Treebank? Zašto je u tokenizatoru napisanom regularnim izrazom važan redoslijed alternativa (kratice, datumi, brojevi)?""",
 r"""<b>Tokenizacija pravilima</b> (engl. <i>rule-based tokenization</i>): unaprijed zadamo <b>standard</b> (što je token) i provedemo ga pravilima, najčešće regularnim izrazima. <b>BPE</b> tokene <b>uči iz podataka</b> (statistikom spajanja) i daje podriječi. Pravila daju predvidljive, cijele riječi koje se mogu objasniti, ali ih treba ručno pisati za svaki jezik.
<b>Kada su pravila bolja:</b> kad trebamo <b>riječi, a ne podriječi</b>, na primjer za parsiranje, označavanje (lematizacija, vrste riječi), lingvističke i društvene analize ili usporedbu s ručno označenim korpusom.

Što standard mora odlučiti: interpunkcija kao zaseban token, ali cijeli Ph.D., AT&amp;T, $45.55, 01/02/06; URL-ovi, #oznake, e-adrese; klitike (what're → what + are). Za hrvatski: decimalni zarez (3,14), točka za tisuće (1.250.000), točka iza rednog broja (15. listopada), kratice (dr. sc., npr., tj., itd.), datumi (15. 10. 2026.) i klitike (reći ću, vidio sam ga).

<b>Banka stabala</b> (engl. <i>treebank</i>) je korpus u kojem je svaka rečenica označena <b>sintaktičkim stablom</b>. <b>Penn Treebank</b> je najpoznatija banka stabala za engleski, a njezin <b>standard tokenizacije</b> je de facto norma: klitike se odvajaju (doesn't → does n't), riječi s crticom ostaju zajedno (San Francisco-based), a sva interpunkcija je zasebno.
```
Ulaz:  "The San Francisco-based restaurant," they said, "doesn't charge $10".
Izlaz: " The San Francisco-based restaurant , " they said , " does n't charge $ 10 " .
```
<b>Redoslijed alternativa je važan</b> jer regularni izraz na svakom položaju isprobava alternative <b>slijeva nadesno i uzima prvu koja uspije</b>, a ne najdulju. Ako bi `\w+` bio ispred kratica, »dr.« bi postao »dr« + ».«; ako bi broj bio ispred datuma, »15. 10. 2026.« raspao bi se na »15«, ».«, »10« … Zato idu redom: kratice → datum → broj → web-adrese → riječi → interpunkcija.
```
pattern = r'''(?xi)
  (?:dr|sc|npr|tj|itd|prof)\.      # kratice
| \d{1,2}\.\s\d{1,2}\.\s\d{4}\.    # datum
| \d+(?:\.\d{3})*(?:,\d+)?         # 1.250,50
| (?:www\.)?\w+(?:\.\w+)+          # web-adrese
| \w+(?:-\w+)*                     # riječi: PDV-a
| [.,;:!?€—()]                     # interpunkcija
'''
nltk.regexp_tokenize(text, pattern)
```
(`(?x)` dopušta razmake i komentare u izrazu, a `i` zanemaruje razliku velikih i malih slova.)"""),

("q3_2", "Segmentacija rečenica: višeznačna točka",
 r"""Segmentacija rečenica: zašto je točka u hrvatskom višeznačna i kako se rečenice mogu odvojiti pravilima?""",
 r"""<b>Segmentacija rečenica</b> je podjela teksta na rečenice. Znakovi ? i ! gotovo su uvijek kraj rečenice, ali <b>točka nije</b>. U hrvatskom točka može biti:
• kraj rečenice;
• dio <b>kratice</b>: dr., sc., npr., tj., itd., prof.;
• <b>redni broj</b>: 5. listopada, 15. 10. 2026., 2. mjesto;
• separator u broju: 1.250.000;
• dio web-adrese ili inicijala: www.mathos.hr, I. G. Kovačić.

<b>Pravilo regularnim izrazom:</b> podijeli tekst na praznini kojoj <b>prethodi</b> . ! ? i iza koje <b>slijedi veliko slovo</b> (pogled unatrag i unaprijed, pa se znakovi ne troše):
```
text = "Sastanak je 5. listopada u 10 h. Dr. Horvat kasni. Dođite na vrijeme!"
re.split(r"(?<=[.!?])\s+(?=[A-ZČĆĐŠŽ])", text)
# ['Sastanak je 5. listopada u 10 h.', 'Dr.', 'Horvat kasni.', 'Dođite na vrijeme!']
re.split(r"(?<!\bDr\.)(?<=[.!?])\s+(?=[A-ZČĆĐŠŽ])", text)      # + kratica
# ['Sastanak je 5. listopada u 10 h.', 'Dr. Horvat kasni.', 'Dođite na vrijeme!']
```
»5. listopada« prolazi jer iza točke slijedi malo slovo. »Dr. Horvat« zahtijeva <b>popis kratica</b> (negativni pogled unatrag) ili model naučen iz podataka. Uspješnost segmentacije mjerimo preciznošću i odzivom granica rečenica u odnosu na zlatni standard."""),

("q3_3", "Konačni automati, formalni i regularni jezik, Kleeneov teorem, DKA/NKA",
 r"""Konačni automati: definirajte konačni automat i objasnite kako prihvaća ili odbacuje string (ovčji jezik). Definirajte abecedu, formalni jezik, jezik automata i regularni jezik. Iskažite Kleeneov teorem i objasnite razliku između determinističkog i nedeterminističkog automata.""",
 r"""<b>Konačni automat</b> (engl. <i>finite-state automaton</i>) ima konačan skup <b>stanja</b>, <b>prijelaze</b> između stanja označene znakovima, jedno <b>početno</b> stanje i jedno ili više <b>prihvatnih</b> stanja.

Automat čita string znak po znak i za svaki znak slijedi odgovarajući prijelaz. <b>Prihvaća</b> string ako nakon zadnjeg znaka stoji u prihvatnom stanju. <b>Odbacuje</b> ga inače, a i onda kad za neki znak nema prijelaza.

<b>Ovčji jezik</b> `baa+!` (baa!, baaa!, …): q0 –b→ q1 –a→ q2 –a→ q3 –!→ <b>q4</b> (prihvatno), uz petlju –a→ na q3.
| znak | – | b | a | a | a | ! |
| stanje | q0 | q1 | q2 | q3 | q3 | q4 ✔ |
»baaa!« je prihvaćen. »ba!« je odbačen, jer u q2 nema prijelaza za !. »baa« je odbačen, jer završava u q3, koje nije prihvatno.
```
delta = {("q0","b"):"q1", ("q1","a"):"q2", ("q2","a"):"q3", ("q3","a"):"q3", ("q3","!"):"q4"}
def accepts(s, start="q0", final={"q4"}):
    q = start
    for c in s:
        q = delta.get((q, c))      # None: nema prijelaza
        if q is None: return False
    return q in final
```
• <b>Abeceda</b> Σ: konačan skup simbola (za ovčji jezik Σ = {a, b, !}).
• <b>Formalni jezik</b>: bilo koji skup stringova nad abecedom Σ, konačan ili beskonačan.
• <b>Jezik automata</b> L(A): skup svih stringova koje automat A prihvaća.
• <b>Regularni jezik</b>: jezik koji prihvaća neki konačni automat. Ovčji jezik je beskonačan, a automat ima samo 5 stanja: konačan opis beskonačnog jezika.

<b>Kleeneov teorem</b> (1956.): skup stringova može se opisati regularnim izrazom <b>ako i samo ako</b> ga prihvaća neki konačni automat. Regularni izrazi i konačni automati jednako su izražajni.

<b>Deterministički automat</b> (DKA) za svako stanje i znak ima <b>najviše jedan</b> prijelaz, pa postoji samo jedan put i jedan korak po znaku (rječnik `delta` to i jamči). <b>Nedeterministički automat</b> (NKA) iz istog stanja za isti znak smije imati <b>više prijelaza</b> ili prijelaz bez znaka (ε). String prihvaća ako <b>barem jedan put</b> završi u prihvatnom stanju. Oba prepoznaju iste jezike: regularni izraz → NKA (Thompsonova konstrukcija) → DKA (konstrukcija podskupova) → brzo prepoznavanje, jedan korak po znaku. Thompson (1968.) je tako ugradio regexe u uređivač ed (naredba g/re/p → alat grep)."""),

("q3_4", "Granice regularnih izraza i Chomskyjeva hijerarhija",
 r"""Granice regularnih izraza: koje jezike regularni izrazi ne mogu opisati (npr. aⁿbⁿ, ugniježđene zagrade) i zašto? Opišite Chomskyjevu hijerarhiju formalnih jezika.""",
 r"""<b>Jezik a<super>n</super>b<super>n</super></b> = {ab, aabb, aaabbb, …} (n puta a, pa <b>isto toliko</b> b) <b>nije regularan</b>. Automat bi morao <b>brojati</b> a-ove da bi provjerio jednako mnogo b-ova, a ima samo konačno mnogo stanja. Za n veći od broja stanja automat mora dva različita broja a-ova »pamtiti« istim stanjem, dakle »zaboravi« koliko ih je bilo, pa prihvati i pogrešne stringove (to je intuicija leme o napuhavanju).

Isti problem postoji i u jeziku:
• <b>ugniježđene zagrade</b> ((( ))): svaka otvorena mora se zatvoriti, a dubina nije ograničena;
• <b>rečenica u rečenici</b>: »Pas [kojeg je mačka [koju je dijete hranilo] ogrebala] laje.«
Pythonov »regex« s povratnom referencom (`(\w+)\s+\1`, »ponovi isto«) zapravo je <b>jači</b> od regularnih izraza u teoriji i opisuje neregularne jezike, zato je ponekad i sporiji.

<b>Chomskyjeva hijerarhija</b> dijeli formalne jezike po izražajnoj snazi; svaka klasa sadrži sve manje:
| klasa | primjer | u jeziku |
| konačni | popis riječi | rječnik |
| regularni | regularni izrazi, ovčji jezik | fonologija, velik dio morfologije |
| kontekstno slobodni | a<super>n</super>b<super>n</super>, ugniježđene strukture | veći dio sintakse |
| blago kontekstno ovisni | križne zavisnosti a<super>n</super>b<super>m</super>c<super>n</super>d<super>m</super> | švicarski njemački |
| kontekstno ovisni | a<super>n</super>b<super>n</super>c<super>n</super> | pravilo ovisi o susjedstvu |
| rekurzivno prebrojivi | sve što prepoznaje Turingov stroj | sve što program može prepoznati |
konačni ⊆ regularni ⊆ kontekstno slobodni ⊆ blago kontekstno ovisni ⊆ kontekstno ovisni ⊆ rekurzivno prebrojivi."""),

("q3_5", "Udaljenost uređivanja, Levenshtein, dinamičko programiranje",
 r"""Udaljenost uređivanja: koje su operacije uređivanja i što je poravnanje? Definirajte Levenshteinovu udaljenost i inačicu u kojoj zamjena košta 2. Zašto se minimalna udaljenost računa dinamičkim programiranjem (tablica D, početni uvjeti, rekurzivna relacija, povratni trag) i kako se koristi za ispravljanje pravopisnih pogrešaka?""",
 r"""<b>Operacije uređivanja</b> su <b>umetanje</b> znaka, <b>brisanje</b> znaka i <b>zamjena</b> jednog znaka drugim. <b>Minimalna udaljenost uređivanja</b> je najmanji broj operacija koje jedan string pretvaraju u drugi (jezk → jezik = 1: umetni i).

<b>Poravnanje</b> (engl. <i>alignment</i>) pridružuje znakove dvaju stringova; * je prazni string. Primjer intention → execution: obriši i, zamijeni n → e, zamijeni t → x, umetni u, zamijeni n → c, ukupno 5 operacija.

<b>Levenshteinova udaljenost</b> (1966.): svaka operacija košta 1, a zamjena znaka istim znakom košta 0. U <b>inačici »zamjena = 2«</b> zamjena vrijedi kao brisanje + umetanje, pa su zapravo dopušteni samo umetanje i brisanje.
| par | zamjena = 1 | zamjena = 2 |
| intention → execution | 5 | 8 |
| pjesma → pisma | 2 | 3 |
| kuča → kuća | 1 | 2 |

<b>Zašto dinamičko programiranje:</b> na svakom koraku ima mnogo mogućih operacija, pa je prostor svih nizova operacija golem (eksponencijalan). No mnogo putova vodi do istog međustringa: podproblemi se <b>preklapaju</b>. Dovoljno je za svaki par prefiksa zapamtiti najkraći put. Dinamičko programiranje (Bellman 1957.) svaki podproblem riješi jednom i spremi ga u tablicu: (n+1)(m+1) ćelija, svaka se računa jednom iz tri susjeda, ukupno ~n·m koraka.

<b>Tablica D:</b> za izvor X duljine n i cilj Y duljine m, D[i, j] je udaljenost između <b>prvih i znakova od X</b> i <b>prvih j znakova od Y</b>. Rješenje je D[n, m].
• <b>Početni uvjeti:</b> D[i, 0] = i (i brisanja), D[0, j] = j (j umetanja).
• <b>Rekurzivna relacija:</b>
$ D[i, j] = min( D[i−1, j] + 1  (brisanje X[i]),   D[i, j−1] + 1  (umetanje Y[j]),   D[i−1, j−1] + z(i, j)  (zamjena) )
$ z(i, j) = 0 ako je X[i] = Y[j], inače 1 (ili 2 u inačici »zamjena = 2«)
Primjer pjesma → pisma (redak = prefiks izvora, stupac = prefiks cilja):
| | # | p | i | s | m | a |
| # | 0 | 1 | 2 | 3 | 4 | 5 |
| p | 1 | <b>0</b> | 1 | 2 | 3 | 4 |
| j | 2 | <b>1</b> | 1 | 2 | 3 | 4 |
| e | 3 | 2 | <b>2</b> | 2 | 3 | 4 |
| s | 4 | 3 | 3 | <b>2</b> | 3 | 4 |
| m | 5 | 4 | 4 | 3 | <b>2</b> | 3 |
| a | 6 | 5 | 5 | 4 | 3 | <b>2</b> |
• <b>Povratni trag</b> (engl. <i>backtrace</i>): u svakoj ćeliji zapamtimo iz kojeg smo susjeda došli. Od D[n, m] slijedimo pokazivače natrag do D[0, 0], a taj put je <b>poravnanje</b>: dijagonalno = zamjena ili isti znak, odozgo (↑) = brisanje, slijeva (←) = umetanje. Za pjesma → pisma: p=p, j→*, e→i, s=s, m=m, a=a.

<b>Ispravljanje pravopisnih pogrešaka:</b> za upisanu riječ izračunamo udaljenost do svih riječi iz rječnika korpusa i predložimo <b>najbližu</b>, a kod jednake udaljenosti <b>češću</b>. jezk → jezik (1), a slijede je (2), jer (2) … Zamjena susjednih slova (hrvatksi → hrvatski) košta 2; inačica s transpozicijom (Damerau) broji je kao 1. Problem: »je« je 400 puta češći od »jezik«, a »sa sestom« → sestrom/šestom (obje na udaljenosti 1). Uz udaljenost trebaju i <b>vjerojatnosti u kontekstu</b>, a to daje jezični model. Rješenje kolokvijskog zadatka: [[z2|Zadatak 2]]."""),
]),
# =====================================================================================
("t4", "4. N-gramski jezični modeli (P5)", "teorija_p5_ngrami.py", [
("q4_1", "Jezični model, pravilo lanca, Markovljeva pretpostavka",
 r"""Definirajte jezični model i iskažite pravilo lanca. Zašto ne možemo procijeniti vjerojatnost riječi uz cijelu povijest? Objasnite Markovljevu pretpostavku za unigramski, bigramski i trigramski model.""",
 r"""<b>Jezični model</b> (engl. <i>language model</i>, LM) za danu povijest h daje vjerojatnost sljedeće riječi P(w | h); množenjem tih vjerojatnosti dobivamo vjerojatnost cijelog niza riječi. Koristi se za ispravljanje pogrešaka (»sa sestrom«), prepoznavanje govora, strojno prevođenje i generiranje teksta; veliki jezični modeli (LLM) uče upravo predvidjeti sljedeći token.

<b>Pravilo lanca</b> (engl. <i>chain rule</i>): vjerojatnost niza je umnožak uvjetnih vjerojatnosti.
$ P(w<sub>1:n</sub>) = P(w<sub>1</sub>) · P(w<sub>2</sub>|w<sub>1</sub>) · P(w<sub>3</sub>|w<sub>1:2</sub>) ⋯ P(w<sub>n</sub>|w<sub>1:n−1</sub>) = ∏<sub>k=1..n</sub> P(w<sub>k</sub>|w<sub>1:k−1</sub>)
Primjer: P(ministar vanjskih poslova) = P(ministar) · P(vanjskih | ministar) · P(poslova | ministar vanjskih).

<b>Zašto ne cijela povijest:</b> pravilo lanca je točno, ali ne pomaže, jer zadnji faktor ima cijelu povijest, a nju ne znamo izbrojati. P(kako | ministar vanjskih poslova izjavio je) bismo procijenili kao C(… je kako) / C(… je), no što je povijest dulja, to je brojeva manje. U korpusu SET »izjavio je« ima 130 pojava, a »ministar vanjskih poslova izjavio je« 0, pa bismo dobili 0/0. Jezik je stvaralački: posve obična rečenica može biti nova. Ni golemi korpusi (Google Web 5-gram, 1 bilijun riječi; infini-gram, 5 bilijuna tokena) nemaju sve povijesti.

<b>Markovljeva pretpostavka</b>: vjerojatnost riječi ovisi samo o <b>nekoliko prethodnih riječi</b>, a ne o cijeloj povijesti (A. A. Markov, 1913., brojio je samoglasnike i suglasnike u »Evgeniju Onjeginu«).
| model | povijest | primjer |
| unigram (n = 1) | nema | P(kako) |
| bigram (n = 2) | 1 riječ | P(kako|je) |
| trigram (n = 3) | 2 riječi | P(kako|izjavio je) |
| n-gram | n − 1 riječi | P(w|n − 1 prethodnih riječi) |
$ bigramski model:  P(w<sub>n</sub>|w<sub>1:n−1</sub>) ≈ P(w<sub>n</sub>|w<sub>n−1</sub>),    P(w<sub>1:n</sub>) ≈ ∏<sub>k</sub> P(w<sub>k</sub>|w<sub>k−1</sub>)
<b>n-gram</b> je niz od n uzastopnih riječi (bigram »izjavio je«, trigram »izjavio je kako«). Isti naziv nosi i model koji riječ predviđa iz n − 1 prethodnih riječi."""),

("q4_2", "MLE, oznake <s> i </s>, zbrajanje logaritama",
 r"""Kako se procjenom najveće vjerodostojnosti računa bigramska vjerojatnost? Čemu služe oznake <s> i </s> i zašto vjerojatnost rečenice računamo zbrajanjem logaritama?""",
 r"""<b>Procjena najveće vjerodostojnosti</b> (engl. <i>maximum likelihood estimation</i>, MLE): vjerojatnosti su <b>relativne frekvencije</b> iz korpusa za učenje, tj. broj n-grama podijeljen brojem (n−1)-grama (povijesti). To su vrijednosti koje korpusu za učenje daju najveću vjerojatnost.
$ P(w<sub>n</sub> | w<sub>n−1</sub>) = C(w<sub>n−1</sub> w<sub>n</sub>) / C(w<sub>n−1</sub>)
Brojnik je koliko puta iza w<sub>n−1</sub> dolazi w<sub>n</sub>, a nazivnik koliko se puta pojavljuje w<sub>n−1</sub>.

Primjer, mali korpus: `<s> ja sam Ana </s>`, `<s> Ana ja sam </s>`, `<s> ja ne volim zelena jaja i šunku </s>`:
| bigram | račun | P |
| P(ja|`<s>`) | C(`<s>` ja) / C(`<s>`) = 2/3 | 0,67 |
| P(Ana|`<s>`) | 1/3 | 0,33 |
| P(sam|ja) | C(ja sam) / C(ja) = 2/3 | 0,67 |
| P(Ana|sam) | 1/2 | 0,5 |
| P(`</s>`|Ana) | 1/2 | 0,5 |

<b>Oznake `<s>` i `</s>`</b> označavaju početak i kraj rečenice.
• `<s>` daje <b>povijest za prvu riječ</b>, pa model zna koje riječi često počinju rečenicu (P(ja | `<s>`)).
• `</s>` omogućuje modelu da »odluči« završiti rečenicu: kraj je jedan od izbora u svakom koraku. Bez nje bi se vjerojatnosti rečenica svake duljine (2, 3, 4 … riječi) zasebno zbrajale u 1, a sve zajedno u beskonačnost. Uz `</s>` sve rečenice dijele jednu vjerojatnost 1, pa je model prava razdioba.

<b>Zašto logaritmi:</b> vjerojatnost rečenice je umnožak mnogo malih brojeva (10 bigrama daje ~1,37·10<super>−16</super>). Za dulje tekstove umnožak postaje premalen za računalo i pretvori se u 0: to je <b>potkoračenje</b> (engl. <i>underflow</i>). Zato zbrajamo log-vjerojatnosti, a zbrajanje je usto brže:
$ p<sub>1</sub> · p<sub>2</sub> · p<sub>3</sub> = exp(log p<sub>1</sub> + log p<sub>2</sub> + log p<sub>3</sub>)"""),

("q4_3", "Vrednovanje: vanjsko/unutarnje, skupovi, perpleksija, faktor grananja",
 r"""Vrednovanje: koja je razlika između vanjskog i unutarnjeg vrednovanja i čemu služe skup za učenje, razvojni i testni skup? Definirajte perpleksiju, objasnite zašto je manja bolja i kako se tumači kao faktor grananja. Zašto model bez izglađivanja može imati beskonačnu perpleksiju?""",
 r"""• <b>Vanjsko vrednovanje</b> (engl. <i>extrinsic</i>): model ugradimo u zadatak (ispravljanje pogrešaka, prepoznavanje govora) i mjerimo uspjeh zadatka. Pouzdano, ali skupo.
• <b>Unutarnje vrednovanje</b> (engl. <i>intrinsic</i>): mjera ovisi samo o modelu, tj. koliko dobro predviđa tekst koji nije vidio. Brzo; najčešće je to perpleksija. Bolja perpleksija ne jamči bolji rezultat u zadatku, pa je dobro potvrditi vanjskim vrednovanjem.

| skup | čemu služi |
| za učenje (training) | brojimo n-grame, tj. procjenjujemo parametre |
| razvojni (dev) | biramo inačicu modela i hiperparametre (k, λ) |
| testni (test) | mjerimo <b>jednom, na kraju</b> |
<b>Kontaminacija podataka:</b> ako testne rečenice završe u skupu za učenje, model ih je »vidio« i rezultat je precijenjen. Zato sve odluke donosimo na razvojnom skupu, a test gledamo što rjeđe.

<b>Perpleksija</b> (PP) je inverz vjerojatnosti testnog skupa, normaliziran brojem riječi N (geometrijska sredina):
$ PP(W) = P(w<sub>1:N</sub>)<super>−1/N</super> = <super>N</super>√( ∏<sub>i=1..N</sub> 1 / P(w<sub>i</sub>|w<sub>i−1</sub>) )
N je broj predviđanja: riječi i `</s>` (kraj se predviđa), ali ne `<s>` (početak je zadan). U Pythonu: `math.exp(-logprob / N)`.

<b>Manja je bolja</b> jer je PP inverz vjerojatnosti: što veću vjerojatnost model daje stvarnom testnom tekstu, to je manje »iznenađen« i perpleksija je manja. Usporedive su samo perpleksije modela s istim rječnikom.

<b>Faktor grananja</b> je broj riječi koje mogu slijediti iza bilo koje riječi; perpleksija je <b>težinski</b> faktor grananja. Primjer: jezik s 3 riječi {crvena, plava, zelena}, test »crvena crvena crvena crvena plava«.
• Model A daje svakoj boji 1/3: PP = ((1/3)<super>5</super>)<super>−1/5</super> = <b>3</b>, kao da bira između 3 riječi.
• Model B daje P(crvena) = 0,8, P(plava) = P(zelena) = 0,1: PP = (0,8<super>4</super>·0,1)<super>−1/5</super> = 0,04096<super>−1/5</super> ≈ <b>1,89</b>. Manje je iznenađen, kao da u prosjeku bira između 1,89 jednako vjerojatnih riječi.
WSJ: unigram 962, bigram 170, trigram 109 (dulja povijest daje manju PP).

<b>Beskonačna perpleksija:</b> dovoljan je <b>jedan</b> bigram iz testa koji se ne pojavljuje u skupu za učenje. MLE mu daje P = 0, pa je cijeli umnožak 0, a PP = 1/0 = ∞ (log 0 = −∞). Na SET-u je takvih 31 % testnih bigrama, pa bigramski i trigramski MLE model imaju PP = ∞ (unigram 388). Rješenje je [[q4_5|izglađivanje]]."""),

("q4_4", "Uzorkovanje, generalizacija, prenaučenost, žanr, <unk>",
 r"""Uzorkovanje i generalizacija: kako se generira rečenica iz modela? Što generirane rečenice govore o modelima različitog reda? Što je prenaučenost, kako na model utječe žanr korpusa i kako se obrađuju nepoznate riječi (<unk>)?""",
 r"""<b>Uzorkovanje</b> (engl. <i>sampling</i>) je slučajan izbor riječi prema vjerojatnostima modela: vjerojatnije riječi biramo češće. Dužinu [0, 1] podijelimo na intervale duljine P(w), izvučemo slučajan broj U i izaberemo riječ u čiji interval broj padne (inverzna transformacija: prva riječ s kumulativnom F(w) ≥ U). Primjer: crvena [0; 0,8), plava [0,8; 0,9), zelena [0,9; 1,0]. Za U = 0,93 izabrana je zelena. U Pythonu se koristi `random.choices(riječi, weights=…)`.

<b>Generiranje rečenice</b> bigramskim modelom: počni s `<s>`, izvuci sljedeću riječ prema P(w | prethodna) i ponavljaj dok ne izvučeš `</s>`.
```
def generate():
    words = ["<s>"]
    while words[-1] != "</s>":
        words.append(next_word(words[-1]))    # random.choices po bigramima
    return " ".join(words[1:-1])
```
<b>Što pokazuju generirane rečenice</b> (SET):
| model | primjer |
| unigram | vlade , djece da Hrvatskoj eura (nepovezane česte riječi) |
| bigram | Zajedno s financijskim odnosima s drugim državama , u Ateni . (lokalno hrvatski, cjelina besmislena) |
| trigram | Kriza će biti veća od zagađenja iz lokalnih gradskih ili industrijskih izvora , navode stručnjaci . |
| 4-gram | Zemlje u ovoj regiji primjenjivale su čitav niz metoda . (cijela rečenica iz korpusa!) |
Što je povijest dulja, to su rečenice suvislije. Ali 4-gramski model na malom korpusu <b>prepisuje korpus</b>, jer za većinu povijesti od 3 riječi postoji samo jedan nastavak.

<b>Prenaučenost</b> (engl. <i>overfitting</i>): model dobro opisuje korpus za učenje, a loše novi tekst.

<b>Žanr:</b> vjerojatnosti nose činjenice o <b>korpusu za učenje</b>. Model naučen na Shakespeareu i model naučen na novinama (WSJ) gotovo nemaju zajedničkih rečenica, a model naučen na vijestima loše predviđa razgovore na forumu. Za vlastiti zadatak treba uzeti korpus istog žanra i iste varijante jezika.

<b>Nepoznate riječi</b> (engl. <i>unknown words</i>, OOV) su riječi testnog skupa kojih nema u rječniku modela; na SET-u je to 13 % testnih tokena. Obrada:
• <b>`<unk>`</b>: zadamo fiksni rječnik, a rijetke riječi u skupu za učenje (npr. one koje se pojave samo jednom) zamijenimo oznakom `<unk>` i brojimo je kao svaku drugu riječ. Na testu svaka nepoznata riječ postaje `<unk>`. (PP tada ovisi o veličini rječnika, pa uspoređujemo modele s istim rječnikom.)
• <b>Podriječi</b> (BPE): nepoznata riječ rastavi se na poznate dijelove; tako rade današnji modeli."""),

("q4_5", "Izglađivanje: Laplace, dodaj-k, interpolacija, (glupo) odstupanje",
 r"""Izglađivanje: što je problem rijetkosti? Objasnite Laplaceovo izglađivanje i izglađivanje dodaj-k (hiperparametar k), interpolaciju (izbor težina λ) te odstupanje i glupo odstupanje. Zašto je na korpusu SET bigramski model s Laplaceom lošiji od unigramskog?""",
 r"""<b>Problem rijetkosti:</b> mnogi sasvim valjani n-grami ne pojavljuju se u korpusu za učenje. Na SET-u nema 31,4 % testnih bigrama i 65,4 % testnih trigrama. MLE im daje 0 (P(rekao | poslova) = 0/95), pa je cijela rečenica vjerojatnosti 0 i PP = ∞. Ni n-grami viđeni jednom ili dvaput nemaju pouzdane procjene. <b>Izglađivanje</b> (engl. <i>smoothing, discounting</i>) oduzme malo vjerojatnosne mase n-gramima koje smo vidjeli i da je onima koje nismo vidjeli.

<b>Laplaceovo izglađivanje</b> (dodaj-1): prije normalizacije svakom broju dodamo 1, i n-gramima koje nismo vidjeli. U nazivnik dodajemo V (veličinu rječnika), jer smo dodali po 1 za svaku od V riječi koje mogu doći iza w<sub>n−1</sub>.
$ P<sub>Laplace</sub>(w<sub>i</sub>) = (c<sub>i</sub> + 1) / (N + V)        P<sub>Laplace</sub>(w<sub>n</sub>|w<sub>n−1</sub>) = (C(w<sub>n−1</sub>w<sub>n</sub>) + 1) / (C(w<sub>n−1</sub>) + V)

<b>Dodaj-k</b>: umjesto 1 dodajemo k &lt; 1 (0,5; 0,01), pa viđeni bigrami gube manje vjerojatnosti. Kao i Laplace, ne razlikuje neviđene bigrame (svi dobiju jednako).
$ P<sub>add−k</sub>(w<sub>n</sub>|w<sub>n−1</sub>) = (C(w<sub>n−1</sub>w<sub>n</sub>) + k) / (C(w<sub>n−1</sub>) + kV)
<b>k je hiperparametar</b>: ne dobivamo ga brojanjem, nego ga biramo na <b>razvojnom skupu</b> (najmanja PP), a test mjerimo samo za izabrani k. SET: k = 1 daje PP 1201,5, a k = 0,01 daje PP 414,6.

<b>Interpolacija</b> (Jelinek i Mercer 1980.): miješamo procjene unigramskog, bigramskog i trigramskog modela s težinama λ. Kad trigrama nema, pomažu bigram i unigram.
$ P̂(w<sub>n</sub>|w<sub>n−2</sub>w<sub>n−1</sub>) = λ<sub>1</sub>P(w<sub>n</sub>) + λ<sub>2</sub>P(w<sub>n</sub>|w<sub>n−1</sub>) + λ<sub>3</sub>P(w<sub>n</sub>|w<sub>n−2</sub>w<sub>n−1</sub>),    Σ λ<sub>i</sub> = 1
<b>Izbor λ</b>: λ su hiperparametri. Biramo one koje razvojnom skupu daju najveću vjerojatnost (pretraga po mreži ili algoritam EM). SET: λ = 0,5 / 0,45 / 0,05 daje PP 191,3, najbolji rezultat. λ<sub>3</sub> je malen jer je korpus premalen da bi trigrami puno pomogli.

<b>Odstupanje</b> (engl. <i>backoff</i>): ako n-grama nema, koristimo (n−1)-gram; ako ni njega nema, još kraći, sve do unigrama. Za pravu vjerojatnost viši n-grami moraju dati popust (Katz).
<b>Glupo odstupanje</b> (engl. <i>stupid backoff</i>; Brants i sur. 2007.) koristi fiksnu težinu λ = 0,4 i završava u unigramu S(w) = C(w)/N:
$ S(w<sub>i</sub>|povijest) = C(povijest w<sub>i</sub>) / C(povijest)  ako je C(povijest w<sub>i</sub>) &gt; 0,   inače  0,4 · S(w<sub>i</sub>|kraća povijest)
Primjer: S(rekao | vanjskih poslova) = 0,4 · 0,4 · 132/159 771 ≈ 0,00013. Rezultat S <b>nije vjerojatnost</b> (ne zbraja se u 1), ali radi dobro na golemim korpusima (web). Razlika od interpolacije: interpolacija <b>uvijek</b> miješa sve redove, a odstupanje koristi kraći model <b>samo kad duljeg nema</b>.

<b>Zašto je Laplace bigram (PP 1201,5) lošiji od unigrama (388,0) na SET-u:</b> rječnik je velik (V = 30 135). Za svaku povijest dodajemo V »izmišljenih« pojava, pa nazivnik C(w<sub>n−1</sub>) + V za većinu riječi postaje skoro samo V. Jedinice za sve neviđene bigrame »pojedu« gotovo svu vjerojatnost, a viđeni bigrami izgube previše: P(je | rekao) pada s 0,71 na 0,0031, čak 227 puta. Model zato daje stvarnim bigramima premalu vjerojatnost i lošije predviđa test od jednostavnog unigrama. Što je n veći, Laplace je još gori (trigram 4732,6).
| model (SET, isti rječnik) | izglađivanje | PP (test) |
| unigram | MLE | 388,0 |
| bigram | MLE | ∞ |
| bigram | Laplace | 1201,5 |
| trigram | Laplace | 4732,6 |
| bigram | dodaj-k, k = 0,01 | 414,6 |
| trigram | interpolacija 0,5/0,45/0,05 | 191,3 |"""),
]),
# =====================================================================================
("t5", "5. Klasifikacija teksta i logistička regresija (P6)", "teorija_p6_klasifikacija.py", [
("q5_1", "Nadzirano učenje, značajke, vreća riječi",
 r"""Što je nadzirano učenje (primjer, oznaka, razred)? Što su značajke, po čemu se razlikuju ručne značajke i vreća riječi i što vreća riječi gubi? Zašto je predviđanje sljedeće riječi zapravo klasifikacija?""",
 r"""<b>Klasifikacija teksta</b> dodjeljuje tekstu oznaku (razred): sentiment, neželjena pošta, jezik, autor, tema, izvor …

<b>Nadzirano učenje</b> (engl. <i>supervised machine learning</i>): iz skupa primjera s poznatim oznakama učimo funkciju f: X → Y koja ulaz x ∈ X preslikava u razred y ∈ Y. Skup za učenje je {(x<super>(1)</super>, y<super>(1)</super>), …, (x<super>(m)</super>, y<super>(m)</super>)}.
• <b>Primjer</b> (engl. <i>observation</i>): jedan ulaz, npr. jedna rečenica.
• <b>Oznaka</b> (engl. <i>label</i>): točan razred tog primjera, npr. »SETimes« ili »hrvatski« (zlatna oznaka). Na SET-u oznake već postoje u podacima (izvor rečenice).
• <b>Razred</b>: jedna od mogućih vrijednosti iz Y, npr. Y = {politika, sport, gospodarstvo}.
Postupak: značajke (tekst → vektor) → model (sigmoid/softmax) → gubitak (unakrsna entropija) → optimizacija (gradijentni spust).

<b>Značajka</b> (engl. <i>feature</i>) je svojstvo ulaza izraženo brojem; ulaz prikazujemo <b>vektorom značajki</b> [x<sub>1</sub>, …, x<sub>n</sub>].
• <b>Ručne značajke</b> biramo sami, iz znanja o zadatku: x<sub>1</sub> = broj riječi »kako« (izjavio je kako …), x<sub>2</sub> = ima li navodnike (1/0), x<sub>3</sub> = broj riječi 1. lica (ja, mi, smo …). »NATO je priopćio kako …« → x = [1, 0, 0]. Ručnih značajki je malo i lako ih je tumačiti, ali traže znanje i mogu promašiti bitno (makro F1 0,60).
• <b>Vreća riječi</b> (engl. <i>bag of words</i>): tekst prikazujemo brojem pojavljivanja <b>svake riječi rječnika</b>, pa je svaka riječ jedna značajka. Značajke ne pišemo ručno, nego model nauči njihovu važnost. Na SET-u ih je 29 572, a vektori su rijetki (rečenica ima dvadesetak riječi). Makro F1 raste na 0,82. U scikit-learnu: `CountVectorizer`.

<b>Što vreća riječi gubi:</b> <b>redoslijed</b> riječi i strukturu rečenice (»nije dobar, nego loš« i »nije loš, nego dobar« imaju istu vreću), doseg negacije i višečlane izraze. Ne zna ni da su riječi slične: »kuna« i »eura« ili »utakmica« i »utakmicu« zasebni su stupci.

<b>Predviđanje sljedeće riječi je klasifikacija:</b> jezični model za danu povijest (ulaz) bira jednu od |V| riječi rječnika (razredi). To je klasifikacija s K = |V| razreda, tj. softmax nad cijelim rječnikom. Na logističkoj regresiji počivaju i neuronske mreže i veliki jezični modeli."""),

("q5_2", "Logistička regresija: težine, pomak, sigmoid, prag, softmax",
 r"""Logistička regresija: objasnite ulogu težina i pomaka u izrazu z = w·x + b i kako se tumači predznak težine. Definirajte sigmoid, njegova svojstva i prag odluke. Kako multinomna logistička regresija softmaxom računa vjerojatnosti za K razreda?""",
 r"""$ z = Σ<sub>i=1..n</sub> w<sub>i</sub>x<sub>i</sub> + b = <b>w</b>·<b>x</b> + b
• <b>Težina</b> w<sub>i</sub> kaže koliko je značajka x<sub>i</sub> važna i za koji razred; <b>w</b>·<b>x</b> je skalarni umnožak. z je »zbroj dokaza« za razred 1.
• <b>Pomak</b> b (engl. <i>bias</i>) je broj koji se dodaje zbroju. Pomiče odluku neovisno o značajkama (kad su sve značajke 0, z = b).
• <b>Predznak težine:</b> pozitivna težina je dokaz za razred 1, negativna za razred 0, a iznos govori koliko je dokaz jak. SET (razred 1 = SETimes): »kako« w<sub>1</sub> = 1,25, navodnici w<sub>2</sub> = 2,04 (dokaz za SETimes), 1. lice w<sub>3</sub> = −1,14 (dokaz za hrvatske izvore), b = −0,62.

<b>Sigmoid</b> (logistička funkcija) preslikava bilo koji realan broj z u interval (0, 1), pa rezultat možemo čitati kao vjerojatnost (sam z ne možemo, jer može biti bilo koji realan broj):
$ σ(z) = 1 / (1 + e<super>−z</super>)
Svojstva: σ(0) = 0,5; strogo raste; velik z → blizu 1, jako negativan z → blizu 0; 1 − σ(z) = σ(−z); derivacija je σ(z)(1 − σ(z)). z se zove i <b>logit</b>, a funkcija daje ime metodi.
$ P(y = 1 | <b>x</b>) = σ(<b>w</b>·<b>x</b> + b),    P(y = 0 | <b>x</b>) = 1 − σ(<b>w</b>·<b>x</b> + b)
<b>Prag odluke</b>: razred 1 ako je P(y = 1 | x) &gt; 0,5, inače razred 0 (to je isto što i z &gt; 0).
• »NATO je priopćio kako …«: z = 1,25·1 + 2,04·0 − 1,14·0 − 0,62 = 0,63; σ(0,63) = 0,65 → SETimes (točno)
• »Ali, napokon smo uspjeli pobjeći.«: z = −1,14 − 0,62 = −1,76; σ(−1,76) = 0,15 → hrvatski (točno)

<b>Multinomna logistička regresija</b> (softmax regresija): svaki od K razreda ima vlastiti vektor težina <b>w</b><sub>k</sub> i pomak b<sub>k</sub>, pa dobijemo K rezultata z<sub>k</sub> = <b>w</b><sub>k</sub>·<b>x</b> + b<sub>k</sub>. Softmax ih pretvara u vjerojatnosti koje su pozitivne i zbrajaju se u 1:
$ softmax(z<sub>i</sub>) = exp(z<sub>i</sub>) / Σ<sub>j=1..K</sub> exp(z<sub>j</sub>),     ŷ = softmax(W<b>x</b> + <b>b</b>)
W je matrica težina s K redaka (po jedan za svaki razred). Primjer s tri izvora: z = (−1,09; 1,31; −0,23) → softmax = (0,07; 0,77; 0,16), pa je odluka »hrvatski portal«. Za tri izvora trebaju tri vektora težina. Jezični model je softmax nad cijelim rječnikom (K = |V|)."""),

("q5_3", "Učenje: unakrsna entropija, gradijentni spust, SGD, epoha",
 r"""Učenje: što je funkcija gubitka i kako glasi unakrsna entropija za binarnu logističku regresiju? Objasnite gradijentni spust, ulogu stope učenja i gradijent (ŷ − y)·xⱼ. Po čemu se stohastički gradijentni spust razlikuje od običnog i što je epoha?""",
 r"""<b>Funkcija gubitka</b> (engl. <i>loss function</i>) mjeri koliko je procjena modela ŷ udaljena od točne oznake y. Učenje traži težine s najmanjim (prosječnim) gubitkom na skupu za učenje.

<b>Unakrsna entropija</b> za binarnu logističku regresiju:
$ L<sub>CE</sub>(ŷ, y) = −[ y log ŷ + (1 − y) log(1 − ŷ) ]
To je negativni logaritam vjerojatnosti koju model daje <b>točnoj</b> oznaci (y je Bernoullijeva varijabla s parametrom ŷ): za y = 1 to je −log ŷ, a za y = 0 to je −log(1 − ŷ). Primjer: model daje ŷ = 0,65 za »NATO je priopćio kako …«. Ako je y = 1 (SETimes), L = −log 0,65 = 0,43; da je rečenica iz hrvatskog izvora (y = 0), bilo bi L = −log 0,35 = 1,06. Savršen model ima gubitak 0, a samouvjerena pogreška se jako kažnjava (ŷ = 0,9 uz y = 0 daje L = 2,30).

<b>Gradijentni spust</b> (engl. <i>gradient descent</i>): težine pomičemo malo po malo u smjeru u kojem gubitak najbrže pada, a to je <b>suprotno od gradijenta</b> (nagiba).
$ w<super>t+1</super> = w<super>t</super> − η · dL/dw,       θ<super>t+1</super> = θ<super>t</super> − η ∇L
Ako je nagib &lt; 0, težinu povećavamo; ako je &gt; 0, smanjujemo je. θ su sve težine i pomak zajedno, a ∇L je vektor gradijenata.

<b>Stopa učenja</b> η (engl. <i>learning rate</i>) određuje koliko velik korak radimo. To je hiperparametar: ako je <b>prevelika</b>, preskačemo minimum (oscilira ili divergira); ako je <b>premalena</b>, učenje traje predugo.

<b>Gradijent za logističku regresiju:</b>
$ ∂L<sub>CE</sub>/∂w<sub>j</sub> = (ŷ − y) · x<sub>j</sub>,       ∂L<sub>CE</sub>/∂b = ŷ − y
• (ŷ − y) je <b>pogreška</b> modela na primjeru, a gradijent za w<sub>j</sub> je pogreška × vrijednost značajke x<sub>j</sub>.
• Ako model griješi više, korak je veći; ako je već točan (ŷ ≈ y), težine se gotovo ne mijenjaju.
• Značajka koje nema u primjeru (x<sub>j</sub> = 0) ne mijenja svoju težinu.
• Ako je ŷ &lt; y (model premalo vjeruje u razred 1), gradijent je negativan pa w<sub>j</sub> raste.
<b>Jedan korak</b> (x = [1, 0, 0], y = 1, početne težine i pomak 0, η = 0,1): z = 0, ŷ = 0,5, pogreška −0,5; gradijent (−0,5, 0, 0), za b −0,5; nakon koraka w = (0,05, 0, 0), b = 0,05. Gubitak pada s 0,6931 na 0,6444. Raste samo težina značajke »kako«, jedine koja se pojavljuje (vidi [[z4|Zadatak 4]]).

<b>Obični (skupni) gradijentni spust</b> računa gradijent na <b>cijelom skupu za učenje</b> (prosjek po svim primjerima) prije svakog koraka: točan smjer, ali spor korak. <b>Stohastički</b> (SGD) popravlja težine nakon <b>svakog pojedinog primjera</b>, slučajnim redoslijedom: brz je, ali »šumovit«. Između je mini-skup (engl. <i>mini-batch</i>). <b>Epoha</b> je jedan prolaz kroz cijeli skup za učenje (na SET-u 6914 rečenica). Zbog slučajnog redoslijeda (shuffle) težine nakon svake epohe nisu iste. Nakon 5 epoha (η = 0,01) težine su [1,27; 2,05; −1,15], b = −0,54, blizu onih iz biblioteke."""),

("q5_4", "Vrednovanje: matrica zabune, P, R, F1, makro prosjek, unakrsna provjera",
 r"""Vrednovanje: što je matrica zabune (tp, fp, fn, tn)? Zašto točnost nije dobra mjera kad razredi nisu uravnoteženi? Definirajte preciznost, odziv, F1 i makro prosjek. Što je unakrsna provjera i kada se koristi?""",
 r"""<b>Matrica zabune</b> (engl. <i>confusion matrix</i>) uspoređuje odluke sustava sa zlatnim (točnim) oznakama. Pozitivan razred je SETimes; vreća riječi + logistička regresija na testnom skupu SET (1036 rečenica):
| | zlatna: SETimes | zlatna: hrvatski |
| sustav: SETimes | tp = 441 (točno pozitivni) | fp = 45 (lažno pozitivni) |
| sustav: hrvatski | fn = 145 (lažno negativni) | tn = 405 (točno negativni) |
$ točnost = (tp + tn) / (tp + fp + tn + fn) = (441 + 405) / 1036 = 0,817

<b>Zamka točnosti:</b> točnost ne kaže <b>koji razred</b> sustav pronalazi. Klasifikator »uvijek SETimes« ima točnost 586/1036 = <b>56,6 %</b>, a ne pronalazi <b>nijednu</b> rečenicu hrvatskih izvora. Kad su razredi neuravnoteženi (npr. 99 : 1), dovoljno je uvijek reći češći razred da točnost bude visoka (99 %), iako je sustav beskoristan za rjeđi razred.

$ preciznost P = tp / (tp + fp)      odziv R = tp / (tp + fn)      F1 = 2PR / (P + R)
• <b>Preciznost</b>: koliko je rečenica koje je sustav pripisao SETimesu doista iz SETimesa.
• <b>Odziv</b>: koliko je rečenica iz SETimesa sustav pronašao.
• <b>F1</b>: harmonijska sredina P i R, bliža <b>manjoj</b> od njih, pa kažnjava neravnotežu.
Primjer: 50 rečenica pripisano SETimesu, od toga 40 točno, a u testu je 80 rečenica iz SETimesa. P = 40/50 = 0,8, R = 40/80 = 0,5, F1 = 2·0,8·0,5/1,3 = <b>0,615</b> (vidi [[z4|Zadatak 4]]).

<b>Makro prosjek</b>: F1 (ili P, R) računamo za svaki razred posebno, pa uzmemo prosjek: F<sub>makro</sub> = (1/K) Σ<sub>k</sub> F<sub>k</sub>. Svaki razred vrijedi jednako, pa slabi razredi snižavaju rezultat. <b>Mikro prosjek</b>: tp, fp i fn zbrojimo preko svih razreda i iz zbrojeva računamo P, R, F1, pa češći razredi više pridonose.
| klasifikator | točnost | F1 SETimes | F1 hrvatski | makro F1 |
| uvijek SETimes | 0,566 | 0,723 | 0,000 | 0,361 |
| LR, 3 značajke | 0,611 | 0,535 | 0,666 | 0,600 |
| LR, vreća riječi | 0,817 | 0,823 | 0,810 | 0,816 |

<b>Unakrsna provjera</b> (engl. <i>cross-validation</i>): podatke podijelimo na k dijelova. k puta učimo na k − 1 dijelova i mjerimo na preostalom, a zatim uzmemo prosjek. Testni skup ostaje netaknut. Koristi se kad je podataka <b>malo</b> pa ne želimo »potrošiti« dio na fiksni razvojni skup, za pouzdaniju procjenu i za odabir hiperparametara (npr. regularizacije C)."""),

("q5_5", "Interpretabilnost, prečaci, kartica modela",
 r"""Interpretabilnost i pogreške: kako se iz težina modela vidi što je model naučio? Što su »prečaci« koje model uči iz korpusa i čemu služi kartica modela?""",
 r"""<b>Interpretabilnost</b> znači da razumijemo zašto je model donio odluku. Kod logističke regresije to čitamo iz <b>težina značajki</b>: riječi s najvećom pozitivnom težinom su najjači dokaz za razred 1 (SETimes), a one s najnegativnijom za razred 0 (hrvatski izvori).
| hrvatski | težina | SETimes | težina |
| kuna | −2,23 | setimes | 2,37 |
| vam | −1,64 | kosova | 2,15 |
| pa | −1,62 | kazao | 2,01 |
| ćete | −1,50 | nato | 1,87 |
| možete | −1,39 | izjavio | 1,58 |
Vidi se da je model naučio <b>teme</b> (kune nasuprot Kosovu, NATO-u, Turskoj) i <b>stil</b> (obraćanje čitatelju »vam, ćete, možete« nasuprot izvještavanju »kazao, izjavio, posebice«). Nitko mu nije rekao pravila, imao je samo oznake rečenica.

<b>Prečaci</b> (engl. <i>shortcuts</i>): model uči <b>statističke sklonosti korpusa</b>, tj. površinske korelacije s oznakom, a ne ono što mi mislimo pod razredom. »Vlada je u ponedjeljak raspravljala o cijeni kruha.« je domaća vijest, ali dobiva P(SETimes) = 0,84 zbog riječi poput »vlada«. Prečac je i sama riječ »setimes« (ime izvora u tekstu). Na novim podacima prečaci ne vrijede, pa model griješi. Moguće štete: sustavi za sentiment i otrovnost lošije postupaju s imenima i jezičnim varijantama manjina, a lažno pozitivne odluke mogu ušutkati govornike određene varijante ili dijalekta.

<b>Kartica modela</b> (engl. <i>model card</i>; Mitchell i sur. 2019.) je dokument uz model koji navodi:
• podatke za učenje i vrednovanje;
• algoritam i parametre;
• namjenu i korisnike (i za što se model <b>ne</b> smije koristiti);
• <b>uspješnost po skupinama</b> (žanrovima, izvorima, demografskim skupinama).
Služi tome da korisnik zna kada se model smije koristiti i gdje griješi, kao što podatkovna kartica opisuje korpus (P2)."""),
]),
# =====================================================================================
("t6", "6. Vektorska semantika i ugradnje (P7)", "teorija_p7_ugradnje.py", [
("q6_1", "Značenje riječi: lema, smisao, odnosi, distribucijska hipoteza, ugradnja",
 r"""Značenje riječi: definirajte lemu, oblik riječi i smisao riječi. Objasnite odnose među riječima (sinonimija, sličnost, povezanost, semantičko polje, konotacija) i razliku između sličnosti i povezanosti. Iskažite distribucijsku hipotezu i objasnite što je ugradnja.""",
 r"""• <b>Lema</b> (engl. <i>lemma</i>): osnovni oblik iz rječnika, npr. <i>miš</i>.
• <b>Oblik riječi</b> (engl. <i>wordform</i>): konkretan oblik u tekstu: miš, miša, mišem, miševi.
• <b>Smisao riječi</b> (engl. <i>word sense</i>): jedno značenje leme. <i>miš</i> ima smisao (1) glodavac i (2) uređaj za pomicanje pokazivača. Lema s više smislova je <b>višeznačna</b>. Vektori iz ovog predavanja grade se po obliku riječi, pa se svi smislovi miješaju u jedan vektor.

| odnos | primjer | što znači |
| sinonimija | kauč – sofa | riječi su zamjenjive (u kontekstu) |
| sličnost | mačka – pas | dijele mnogo svojstava |
| povezanost | kava – šalica | pojavljuju se zajedno, u istoj situaciji |
| semantičko polje | kirurg, skalpel, bolnica | riječi iste domene |
| konotacija | kopija – krivotvorina | drukčiji vrijednosni (afektivni) stav |
Osgood (1957.) je konotaciju prikazao trima brojevima (ugodnost, pobuđenost, dominacija), pa je riječ točka u prostoru.

<b>Sličnost ili povezanost:</b> kava i čaj su <b>slični</b> (oba su napitci, mogu jedan drugog zamijeniti), a kava i šalica su <b>povezani</b> (pojavljuju se zajedno), ali nisu slični. SimLex-999 mjeri samo sličnost (cup–mug visoko, cup–coffee nisko). Ugradnje iz konteksta hvataju i sličnost i povezanost, ali ih <b>ne razlikuju</b>: kava–šalica bit će blizu kao kava–čaj.

<b>Distribucijska hipoteza</b> (Harris 1954., Firth 1957.): riječi koje se pojavljuju u <b>sličnim kontekstima</b> imaju <b>slično značenje</b> (»Riječ ćeš upoznati po društvu u kojem se nalazi.«). Primjer: »raštika« se pojavljuje uz iste riječi kao blitva i kelj (krumpir, ulje, tržnica, listovi, skuhati), pa je vjerojatno lisnato povrće.

<b>Ugradnja</b> (engl. <i>embedding</i>) je vektor koji predstavlja značenje riječi, naučen iz njezine distribucije u tekstu; slične riječi su bliske točke u prostoru. Spaja dvije ideje iz 1950-ih: distribuciju (značenje određuju riječi oko nje) i prostor (značenje je točka u višedimenzionalnom prostoru, Osgood). Ugradnje se uče bez ručnih oznaka, samo iz teksta: model sam nauči značajke (učenje reprezentacije), a ne biramo ih ručno kao u P6. Područje se zove <b>vektorska semantika</b>."""),

("q6_2", "Matrica riječ–kontekst, prozor, kosinus, PMI i PPMI",
 r"""Vektori riječi iz brojanja: kako se gradi matrica riječ–kontekst i kako veličina prozora utječe na rezultat? Zašto za sličnost koristimo kosinus, a ne skalarni umnožak? Zašto česte riječi kvare vektore iz brojanja? Definirajte PMI i PPMI, protumačite ih i navedite slabost PMI-ja kod rijetkih parova.""",
 r"""<b>Matrica riječ–kontekst</b>: redak je ciljna riječ, stupac kontekstna riječ, a ćelija broj pojavljivanja konteksta u <b>prozoru</b> oko ciljne riječi. Za svaku pojavnicu ciljne riječi pogledamo npr. 4 riječi lijevo i 4 desno i svakoj dodamo 1 u njezin stupac. Redak je <b>vektor riječi</b> duljine |V| (~30 000).
| | milijuna | milijardi | oko | izjavio | siječnja | ( |
| kuna | 62 | 22 | 11 | 0 | 0 | 6 |
| eura | 67 | 27 | 25 | 0 | 0 | 4 |
| ponedjeljak | 0 | 0 | 0 | 10 | 7 | 40 |
| utorak | 0 | 0 | 0 | 6 | 6 | 28 |
<b>Veličina prozora</b> je naš izbor. <b>Manji</b> prozor (±1–3) daje riječi <b>iste vrste</b>, sintaktički slične (kuna – eura). <b>Veći</b> prozor (±5–10) daje riječi <b>iste teme</b> (kuna – banka).

<b>Kosinus, a ne skalarni umnožak:</b> skalarni umnožak <b>v</b>·<b>w</b> = Σ v<sub>i</sub>w<sub>i</sub> velik je i kad su vektori samo <b>dugi</b>, a duljina vektora ovisi o <b>učestalosti</b> riječi. Česte riječi bile bi tada »slične« svemu. Za sličnost nas zanima <b>smjer</b>, pa mjerimo kut:
$ cos(<b>v</b>, <b>w</b>) = <b>v</b>·<b>w</b> / (|<b>v</b>| |<b>w</b>|),      |<b>v</b>| = √(Σ v<sub>i</sub><super>2</super>)
Za brojeve ≥ 0 kosinus je između 0 i 1. [1, 0, 2] i [2, 0, 4] imaju kosinus 1 (isti smjer, drugačija duljina). cos(kuna, eura) = 5047 / (66,97 · 76,54) = <b>0,985</b>; cos(kuna, ponedjeljak) = 240 / (66,97 · 41,82) = <b>0,086</b>.

<b>Česte riječi kvare vektore:</b> najčešći konteksti gotovo svake riječi su zarez, »je«, »i«, »u«. Oni ne govore ništa o samoj riječi, a imaju najveće brojeve, pa dominiraju vektorom (za »grčka«: zarez 21, je 8, i 7, a korisni konteksti bugarska, rusija, sporazum samo po 3). Zato je »grčka« po kosinusu sirovih brojeva najbliža veznicima (a, no, ali, dok, međutim), jer i veznici i države najčešće stoje uz zarez i »je«.

<b>PMI</b> (točkovna uzajamna informacija) mjeri pojavljuju li se w i c zajedno <b>češće nego slučajno</b>, tj. nego da su neovisni (tada bi P(w,c) = P(w)P(c)):
$ PMI(w, c) = log<sub>2</sub> [ P(w, c) / (P(w) · P(c)) ],     P(w,c) = broj(w,c)/N,  P(w) = broj(w)/N,  P(c) = broj(c)/N
$ PPMI(w, c) = max(PMI(w, c), 0)
<b>Tumačenje:</b> 0 znači kao slučajno, 1 dvaput češće, 2 četiri puta češće, a −1 upola rjeđe. Primjer: PMI(grčka, rusija) = log<sub>2</sub>(3 · 1 415 250 / (176 · 216)) = log<sub>2</sub> 111,7 = <b>6,80</b> (112 puta češće nego slučajno), a PMI(grčka, u) = −0,83, pa je PPMI = 0. Negativne vrijednosti su na malom korpusu nepouzdane (»rjeđe nego slučajno« traži golem korpus), pa ih PPMI postavlja na 0. S PPMI-jem su susjedi riječi »grčka« države: njemačka, italija, cipar, španjolska.

<b>Slabost PMI-ja:</b> <b>precjenjuje rijetke parove</b>. Ako su w i c rijetki, jedno slučajno zajedničko pojavljivanje daje vrlo mali nazivnik P(w)P(c) i golem omjer, pa najveće vrijednosti dobivaju rijetke riječi. Lijekovi: brojati samo kontekste viđene barem 2 puta, izgladiti P(c) potencijom α = 0,75 ili dodati k brojevima (Laplace)."""),

("q6_3", "Matrica riječ–dokument, tf-idf, pretraživanje, LSA",
 r"""Vektori dokumenata: kako se gradi matrica riječ–dokument? Definirajte tf, idf i tf-idf i objasnite koja riječ ima idf 0. Kako se tf-idf koristi za pretraživanje i koje je njegovo ograničenje za hrvatski? Objasnite latentnu semantičku analizu: što je vektor dokumenta, kako LSA povezuje dokumente bez zajedničkih riječi i kako broj tema utječe na rezultat.""",
 r"""<b>Matrica riječ–dokument</b> (engl. <i>term-document matrix</i>): isto brojanje, ali stupac je <b>dokument</b>, a ćelija broj pojavljivanja riječi u dokumentu. Stupac je <b>vektor dokumenta</b>; i upit je vektor. Problemi sirovih brojeva: riječi »je«, »godine« nose najveće brojeve, pa i vijesti o posve različitim temama izgledaju slično (kosinus 0,39–0,53). Usto 11 pojavljivanja nije 11 puta važnije od jednog.

$ tf(t, d) = log<sub>10</sub>(broj(t, d) + 1)
<b>tf</b> (čestota riječi) prigušuje velike brojeve: deset puta više pojavljivanja dodaje samo 1. +1 je tu da riječ koje nema dobije 0 (log 1 = 0). tf(nataliteta, D1) = log<sub>10</sub>12 = 1,08; za 9 pojavljivanja tf = 1.
$ idf(t) = log<sub>10</sub>(N / df(t))
<b>idf</b> (obrnuta čestota u dokumentima): N je broj dokumenata (249), a df(t) broj dokumenata u kojima je riječ t. Riječi rijetke u zbirci su važnije: idf(je) = log(249/248) = 0,002, a idf(nataliteta) = log(249/1) = 2,40.
$ tfidf(t, d) = tf(t, d) · idf(t)
<b>tf-idf</b> je velik kad je riječ <b>česta u dokumentu, a rijetka u zbirci</b>: tfidf(nataliteta, D1) = 1,08 · 2,40 = 2,59, a tfidf(je, D1) ≈ 0. Kosinus između različitih vijesti pada na 0,01–0,03.

<b>idf = 0</b> ima riječ koja se pojavljuje <b>u svim dokumentima</b> (df = N, log 1 = 0). To je dobro za pretraživanje: takva riječ ne razlikuje dokumente, pa se automatski zanemaruje (kao »je«).

<b>Pretraživanje:</b> dokumente i upit prikažemo tf-idf vektorima, izračunamo <b>kosinus</b> upita sa svakim dokumentom i vratimo dokumente poredane po kosinusu. Upit »utakmica«: »Skandal oko namještanja nogometnih utakmica« 0,57 itd. (scikit-learn: `TfidfVectorizer`, `cosine_similarity`; na testu samo `transform`).

<b>Ograničenje za hrvatski:</b> tf-idf uspoređuje <b>točne oblike</b> riječi. »utakmica«, »utakmicu« i »utakmice« za njega su nepovezane riječi, pa vijest o grčkom treneru (»… izgubio utakmicu …«) dobiva 0. Zbog bogate fleksije to je u hrvatskom mnogo češće nego u engleskom. Ne prepoznaje ni sinonime (trener, igrači …). Pomaže lematizacija, podriječi ili gusti vektori.

<b>Latentna semantička analiza</b> (LSA; Deerwester i sur. 1990.): riječi koje se pojavljuju u istim dokumentima spoji u jednu dimenziju, <b>temu</b>. Matricu dokumenti × riječi (tf-idf) X rastavimo SVD-om i zadržimo k najvažnijih tema (npr. 50):
$ X (249 × 9401) ≈ U (249 × 50) · Σ (50 × 50) · V<super>T</super> (50 × 9401)
<b>Vektor dokumenta</b> u LSA je <b>z</b><sub>d</sub> = (<b>x</b><sub>d</sub>·<b>v</b><sub>1</sub>, …, <b>x</b><sub>d</sub>·<b>v</b><sub>50</sub>), 50 brojeva. Svaki broj kaže <b>koliko dokument sadrži jednu temu</b> (tf-idf težine njegovih riječi pomnožene težinama riječi u temi). Upit dobiva vektor na isti način (`lsa.transform`).

<b>Povezivanje bez zajedničkih riječi:</b> vijest o treneru nema riječ »utakmica«, ali ima »trener«, »reprezentacije«, »igrača«. To su riječi koje u zbirci stoje uz »utakmica«, pa sve imaju pozitivnu težinu u istoj temi (tema 27: utakmica 0,154, kluba 0,042, igrača 0,037, trener 0,020). I upit i vijest imaju pozitivnu komponentu te teme, pa je kosinus 0,29 (s tf-idf-om 0).

<b>Broj tema:</b> <b>premalo</b> tema daje grube teme koje miješaju nepovezane stvari, pa ima lažnih veza (»Manjinske zaklade« 0,33 uz upit »utakmica«). <b>Previše</b> tema približava se tf-idf-u: gubi se poopćavanje i ostaje šum. Broj tema biramo pokusom (na vježbama 10/100/200)."""),

("q6_4", "Gusti vektori, word2vec skip-gram, negativno uzorkovanje, fastText",
 r"""Gusti vektori: koje su prednosti gustih vektora pred rijetkima? Zašto word2vec ne predviđa kontekst softmaxom po cijelom rječniku? Objasnite skip-gram kao binarni klasifikator (samonadzirano učenje, protuprimjeri), njegov gubitak i gradijent te kako se vektori mijenjaju u jednom koraku. Kako fastText gradi vektor riječi, zašto je koristan za hrvatski i kada griješi?""",
 r"""| | rijetki (brojanje, PPMI) | gusti (ugradnje) |
| duljina | veličina rječnika: 10 000 – 50 000 | 50 – 300 |
| vrijednosti | gotovo sve 0 (»grčka«: 69 od 2361 nije 0) | sve različite od 0, pozitivne i negativne |
| dimenzija | jedna dimenzija = jedna riječ | dimenzije nemaju ime; značenje nosi cijeli vektor |
| »auto« i »automobil« kao konteksti | dva nepovezana stupca | slični vektori |
<b>Prednosti gustih vektora:</b> klasifikator koji ih koristi treba mnogo manje težina, pa bolje poopćava i manje se prenauči. Bolje hvataju sinonimiju (slične riječi dijele dimenzije), brže se računa i u praksi rade bolje.

<b>Zašto ne softmax:</b> zadatak word2veca je iz ciljne riječi predvidjeti koja riječ stoji u njezinu prozoru. Najprirodnije bi bilo klasificirati u onoliko razreda koliko ima riječi:
$ P(c | w) = exp(<b>c</b>·<b>w</b>) / Σ<sub>c′∈V</sub> exp(<b>c′</b>·<b>w</b>)
Nazivnik zbraja po <b>cijelom rječniku za svaki par</b> (riječ, kontekst). Na SET-u je to 5224 skalarnih umnožaka po paru, uz oko 1,4 milijuna parova po epohi; za rječnike od milijun riječi to je neizvedivo. Umjesto toga pitamo binarno »je li c susjed od w?« (sigmoid) i dodamo samo nekoliko nasumičnih riječi kao primjere za »ne«: 1 + 5 = 6 skalarnih umnožaka, 870 puta manje.

<b>Skip-gram kao binarni klasifikator.</b> <b>Samonadzirano učenje</b> (engl. <i>self-supervision</i>) znači da oznake dobivamo iz samog teksta, bez ručnog označavanja. Za ciljnu riječ »ministar« (prozor ±2) u »… izjavio je izraelski <b>ministar</b> vanjskih poslova …«:
• <b>pozitivni primjeri</b> (y = 1) su stvarni susjedi: ministar–je, ministar–izraelski, ministar–vanjskih, ministar–poslova;
• <b>protuprimjeri</b> (y = 0; negativno uzorkovanje) su nasumične riječi iz rječnika: ministar–napredak, ministar–grada. Bez njih bi model naučio da je svaka riječ susjed (svi vektori jednaki).
$ ŷ = P(susjed | w, c) = σ(<b>c</b>·<b>w</b>) = 1 / (1 + exp(−<b>c</b>·<b>w</b>))
To je logistička regresija iz P6, ali se <b>obje strane skalarnog umnoška uče</b> (ugradnja ciljne riječi <b>w</b> i kontekstne <b>c</b>), a cilj nisu oznake nego vektori.

<b>Gubitak i gradijent</b> (unakrsna entropija kao u P6, isti oblik: (ŷ − y) · »ulaz«):
$ L = −[ y log ŷ + (1 − y) log(1 − ŷ) ],     ∂L/∂<b>c</b> = (ŷ − y) <b>w</b>,     ∂L/∂<b>w</b> = (ŷ − y) <b>c</b>
$ <b>c</b> ← <b>c</b> − η(ŷ − y)<b>w</b>,       <b>w</b> ← <b>w</b> − η(ŷ − y)<b>c</b>
• y = 1 (stvarni susjed): ŷ − y &lt; 0, pa se <b>c</b> pomiče <b>prema</b> <b>w</b> i <b>c</b>·<b>w</b> raste.
• y = 0 (nasumična riječ): ŷ − y &gt; 0, pa se <b>c</b> <b>odmiče</b> od <b>w</b> i <b>c</b>·<b>w</b> pada.
<b>Jedan korak</b> (dvije dimenzije, η = 1, y = 1): <b>w</b> = [1; 0], <b>c</b> = [0; 1], ŷ = σ(0) = 0,5. Novi <b>c</b> = [0; 1] + 0,5·[1; 0] = [0,5; 1], novi <b>w</b> = [1; 0] + 0,5·[0; 1] = [1; 0,5]. Sada je <b>c</b>·<b>w</b> = 1 i ŷ = σ(1) = 0,73: susjedi su se približili. Korak se ponavlja za sve parove kroz više epoha (ministar–napredak: 0,53 → 0,11).

<b>fastText</b> (Bojanowski i sur. 2017.): vektor riječi je <b>zbroj vektora njezinih dijelova</b>, tj. znakovnih n-grama (s oznakama &lt; i &gt; za početak i kraj) i cijele riječi. Vektori dijelova uče se istim skip-gramom.
$ <b>v</b>(utakmica) = <b>z</b>(&lt;ut) + <b>z</b>(uta) + <b>z</b>(tak) + … + <b>z</b>(ca&gt;) + <b>z</b>(&lt;utakmica&gt;)
<b>Koristan za hrvatski:</b> imenica ima do 14 oblika, a mnogi su rijetki ili ih u korpusu nema, pa word2vec za njih nema (dobar) vektor. »utakmica« i »utakmicu« dijele 6 od 8 trigrama, pa su im vektori slični. Nepoznati oblik nema vlastiti vektor, ali dobije zbroj vektora svojih dijelova (veza s podriječima i BPE-om), a to je upravo ono što tf-idf nije znao.
<b>Kada griješi:</b> kad je oblik sličan, a značenje nije: riječi s istim nastavcima ili slovima (pas – pasta – pasti, kosa – kos) dobiju slične vektore. Griješi i kod kratkih riječi s malo n-grama, imena i posuđenica, te kod višeznačnih riječi (jedan vektor za sve smislove, npr. miš)."""),

("q6_5", "Što ugradnje znaju: PCA, analogije, pristranost, vrednovanje",
 r"""Što ugradnje znaju: što pokazuje vizualizacija ugradnji metodom glavnih komponenti i koja su njezina ograničenja? Objasnite analogije i model paralelograma te kada rade. Zašto ugradnje mogu biti pristrane (pogreška raspodjele i pogreška prikaza)? Koja je razlika između vanjskog i unutarnjeg vrednovanja ugradnji?""",
 r"""<b>Vizualizacija metodom glavnih komponenti</b> (PCA): ugradnje (npr. 100 dimenzija) spljoštimo na <b>dvije dimenzije</b>, tj. dva smjera u kojima se odabrane ugradnje najviše razlikuju (1. i 2. glavna komponenta). Pokazuje da slične riječi tvore skupine: dani i mjeseci, države, novac i film nalaze se u zasebnim skupinama, a model je to naučio samo iz konteksta.
<b>Ograničenja:</b> projekcija s 100 na 2 dimenzije gubi informaciju, pa riječi bliske na slici ne moraju biti bliske u 100 dimenzija (i obrnuto). Osi nemaju jedinicu ni izravno značenje. Slika ovisi o odabranim riječima, a skupine (boje) biramo mi, ne model.

<b>Analogije i model paralelograma</b> (Rumelhart i Abrahamson 1973.): <b>razlika vektora kodira odnos</b> (muško → žensko, država → glavni grad). Analogiju a : b = a* : ? rješavamo tako da potražimo riječ najbližu vektoru <b>b</b> − <b>a</b> + <b>a*</b> (kosinusom, bez samih ulaznih riječi):
$ <b>v</b>(kralj) − <b>v</b>(muškarac) + <b>v</b>(žena) ≈ <b>v</b>(kraljica)        <b>v</b>(Pariz) − <b>v</b>(Francuska) + <b>v</b>(Italija) ≈ <b>v</b>(Rim)
Zagreb : Hrvatska = Beč : x  →  <b>x</b> ≈ <b>v</b>(Hrvatska) − <b>v</b>(Zagreb) + <b>v</b>(Beč) → Austrija.
<b>Kada rade:</b> za <b>česte riječi</b> i <b>neke odnose</b> (glavni grad, rod, glagolsko vrijeme, množina), i to na ugradnjama naučenim na <b>milijardama riječi</b>. Ne rade općenito: na malom korpusu SET atena − grčka + turska daje »registar, odobriti, razdoblje …«.

<b>Pristranost:</b> ugradnje uče iz teksta koji su napisali ljudi, pa uče i <b>stereotipe</b> iz tog teksta, iako ih nitko nije ručno označio. Primjeri: programer − muškarac + žena ≈ kućanica; otac : liječnik = majka : medicinska sestra (Bolukbasi i sur. 2016.); imena tipična za neke etničke skupine bliža su neugodnim riječima (Caliskan i sur. 2017.); ugradnje čak <b>pojačavaju</b> pristranost iz podataka (Zhao i sur. 2017.).
• <b>Pogreška raspodjele</b> (engl. <i>allocational harm</i>): sustav nepravedno raspodjeljuje resurse ili prilike, npr. sustav za zapošljavanje lošije rangira žene.
• <b>Pogreška prikaza</b> (engl. <i>representational harm</i>): sustav ponižava, stereotipizira ili zanemaruje skupinu.
Za hrvatski: zanimanja imaju muški i ženski oblik (liječnik / liječnica), a kosinusom mjerimo koje su im riječi najbliže.

<b>Vrednovanje ugradnji</b>
• <b>Vanjsko</b>: ugradnje uključimo u <b>zadatak</b> (npr. klasifikaciju iz P6) i mjerimo pomažu li. To je najvažnije.
• <b>Unutarnje</b>: ugradnje ocjenjujemo izravno, uspoređujući kosinuse s <b>ljudskim procjenama sličnosti</b> (mjera je korelacija) ili rješavajući analogije. Skupovi podataka: WordSim-353 (353 para imenica s ocjenama 0–10), SimLex-999 (samo sličnost, ne povezanost), TOEFL (80 pitanja: najbliži sinonim od 4 ponuđena), analogije (glavni gradovi, množina, rod).
Oprez: word2vec pri svakom učenju daje malo drukčije vektore (slučajnost), pa rezultate treba ponoviti."""),
]),
]

FORMULAS = [
("Heaps", r"|V| = k · N<super>β</super>, 0 &lt; β &lt; 1"),
("UTF-8 (2 bajta)", r"110yyyyy 10xxxxxx; č = U+010D = C4 8D"),
("Levenshtein", r"D[i,0]=i, D[0,j]=j; D[i,j] = min(D[i−1,j]+1, D[i,j−1]+1, D[i−1,j−1]+z), z = 0 ili 1 (2)"),
("pravilo lanca", r"P(w<sub>1:n</sub>) = ∏ P(w<sub>k</sub>|w<sub>1:k−1</sub>)"),
("bigram MLE", r"P(w<sub>n</sub>|w<sub>n−1</sub>) = C(w<sub>n−1</sub>w<sub>n</sub>) / C(w<sub>n−1</sub>)"),
("perpleksija", r"PP = P(w<sub>1:N</sub>)<super>−1/N</super> = exp(−(1/N) Σ log P)"),
("Laplace / dodaj-k", r"(C(w<sub>n−1</sub>w<sub>n</sub>) + k) / (C(w<sub>n−1</sub>) + kV), Laplace: k = 1"),
("interpolacija", r"λ<sub>1</sub>P(w<sub>n</sub>) + λ<sub>2</sub>P(w<sub>n</sub>|w<sub>n−1</sub>) + λ<sub>3</sub>P(w<sub>n</sub>|w<sub>n−2</sub>w<sub>n−1</sub>), Σλ = 1"),
("glupo odstupanje", r"S = C(n-gram)/C(povijest) ako &gt; 0, inače 0,4 · S(kraća povijest)"),
("logistička regresija", r"z = <b>w</b>·<b>x</b> + b, ŷ = σ(z) = 1/(1 + e<super>−z</super>), razred 1 ako ŷ &gt; 0,5"),
("softmax", r"softmax(z<sub>i</sub>) = exp(z<sub>i</sub>) / Σ<sub>j</sub> exp(z<sub>j</sub>)"),
("unakrsna entropija", r"L = −[y log ŷ + (1−y) log(1−ŷ)]"),
("gradijent", r"∂L/∂w<sub>j</sub> = (ŷ − y)x<sub>j</sub>, ∂L/∂b = ŷ − y, w ← w − η∂L/∂w"),
("P, R, F1", r"P = tp/(tp+fp), R = tp/(tp+fn), F1 = 2PR/(P+R)"),
("kosinus", r"cos(<b>v</b>,<b>w</b>) = <b>v</b>·<b>w</b> / (|<b>v</b>||<b>w</b>|)"),
("PMI / PPMI", r"log<sub>2</sub> P(w,c)/(P(w)P(c)); PPMI = max(PMI, 0)"),
("tf-idf", r"tf = log<sub>10</sub>(broj+1), idf = log<sub>10</sub>(N/df), tfidf = tf·idf"),
("skip-gram", r"ŷ = σ(<b>c</b>·<b>w</b>); <b>c</b> ← <b>c</b> − η(ŷ−y)<b>w</b>, <b>w</b> ← <b>w</b> − η(ŷ−y)<b>c</b>"),
("fastText", r"<b>v</b>(w) = Σ<sub>g∈G(w)</sub> <b>z</b>(g)  (znakovni n-grami + cijela riječ)"),
("analogija", r"<b>x</b> ≈ <b>b</b> − <b>a</b> + <b>a*</b>  (kralj − muškarac + žena ≈ kraljica)"),
]
