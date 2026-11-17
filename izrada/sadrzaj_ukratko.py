"""Opušteniji sloj za PDF s teorijom: uvod u svaku temu i »ukratko« za svako pitanje."""

INTROS = {
    "t1": "Prije nego što model išta »razumije«, mora tekst izrezati na komadiće. Ovdje saznaješ što je uopće "
          "riječ, zašto je č računalu dva bajta i zašto hrvatski tokenizatorima zadaje glavobolju.",
    "t2": "Regularni izrazi izgledaju kao da je mačka prošetala tipkovnicom, ali jednom kad ih »pročitaš«, "
          "postaju najkorisniji alat za tekst. Uvijek `r\"…\"` i polako.",
    "t3": "Regex na djelu (tokenizator, rečenice), teorija ispod haube (automati) i odgovor na vječno pitanje: "
          "koliko je »jezk« daleko od »jezik«?",
    "t4": "Kako izračunati koliko je rečenica vjerojatna? Brojanjem. Puno brojanja. I malo varanja kad brojevi "
          "ispadnu nula (izglađivanje).",
    "t5": "Logistička regresija je djed svih neuronskih mreža: zbroji dokaze, stisni ih sigmoidom, popravi se "
          "gradijentom. Plus: kako ne povjerovati točnosti koja laže.",
    "t6": "Riječi kao točke u prostoru: »kuna« i »eura« žive u istom kvartu, a »ponedjeljak« na drugom kraju grada. "
          "Od brojanja susjeda do word2veca i fastTexta.",
}

# Ukratko: jedna-dvije rečenice koje treba zapamtiti (pa onda pročitaj ostatak)
TLDR = {
    "q1_1": "Pojavnice broje <b>sve</b>, različnice samo <b>različito</b>. Rječnik nikad ne prestaje rasti (Heaps), "
            "a hrvatski sa svojim padežima raste još brže.",
    "q1_2": "Morfem = najmanji komadić sa značenjem. Fleksija mijenja oblik (knjiga → knjizi), tvorba radi novu riječ "
            "(čitati → čitatelj). Hrvatski = <b>sintetički + fuzijski</b>.",
    "q1_3": "Unicode svakom znaku da broj, UTF-8 taj broj zapiše u 1–4 bajta. <b>č = U+010D = C4 8D = 2 bajta</b>. "
            "Pazi: č se može zapisati na dva načina, a NFC to pospremi.",
    "q1_4": "BPE: spoji najčešći par, ponovi k puta. Bajtovi = nema nepoznatih znakova; predtokenizacija = ne spajaj "
            "preko granica riječi.",
    "q1_5": "Tokenizatori su »odrasli« na engleskom pa hrvatski sjeckaju na sitno (2,71 tokena po riječi). "
            "Podatkovna kartica = osobna iskaznica korpusa.",
    "q2_1": "Regex = opis <b>skupa stringova</b>. Piši `r\"…\"` da Python ne pojede obrnute kose crte. "
            "search = prvi, findall = svi, sub = zamijeni, split = razreži.",
    "q2_2": "`[a-z]` ide po kodnim točkama, a č živi daleko iza z. Zato `\\w` ili `[a-zčćđšž]`.",
    "q2_3": "`? * + {n,m}` = koliko puta; `.` = bilo što; `^ $ \\b` = gdje. Pohlepno grabi najviše, "
            "nepohlepno (`*?`) najmanje.",
    "q2_4": "Kvantifikator veže jače od niza, a niz jače od `|`. Zato `je*` nije `(je)*`, a `mačka|ke` nije `mačk(a|e)`. "
            "Lažno pozitivni ruše preciznost, lažno negativni odziv.",
    "q2_5": "Zagrade pamte, `\\1` vraća. Lookahead gleda bez diranja. ELIZA = niz `re.sub`-ova; hrvatski treba "
            "puno više pravila zbog slaganja (tužan/tužna).",
    "q3_1": "Pravila: <b>ti</b> odlučuješ što je token. BPE: <b>podaci</b> odlučuju. U regexu pobjeđuje prva "
            "alternativa koja uspije, zato kratice i datumi idu prvi.",
    "q3_2": "Točka u hrvatskom ima previše poslova: kraj rečenice, kratica, redni broj… Pravilo: reži gdje iza "
            ". ! ? dolazi veliko slovo, plus popis kratica.",
    "q3_3": "Automat = stanja + strelice. Ako nakon zadnjeg znaka stojiš u prihvatnom stanju, prihvaćeno. "
            "Kleene: regex i automat su ista stvar u drugom ruhu.",
    "q3_4": "Automat ne zna brojati, pa aⁿbⁿ i ugniježđene zagrade otpadaju. "
            "Chomsky: konačni ⊂ regularni ⊂ kontekstno slobodni ⊂ … ⊂ rekurzivno prebrojivi.",
    "q3_5": "Najmanje umetanja, brisanja i zamjena. Tablica D: svaka ćelija je minimum od tri susjeda. "
            "<b>pjesma → pisma = 2</b>.",
    "q4_1": "Jezični model odgovara na pitanje »koja riječ ide sljedeća?«. Cijela povijest je prerijetka, pa Markov "
            "kaže: gledaj samo zadnjih n − 1 riječi.",
    "q4_2": "MLE = prebroji i podijeli. `<s>` i `</s>` = početak i kraj. Logaritmi zato što bi umnožak sitnih "
            "brojeva postao nula.",
    "q4_3": "Uči na trainu, biraj na devu, mjeri <b>jednom</b> na testu. Perpleksija = koliko je model zbunjen; "
            "manje je bolje. Jedna nula i eto ∞.",
    "q4_4": "Generiranje = bacanje kocke po vjerojatnostima. Veći n = smislenije, ali na malom korpusu samo "
            "prepisuje. `<unk>` za neznance.",
    "q4_5": "Izglađivanje = uzmi bogatima, daj siromašnima. Laplace daje <b>previše</b> siromašnima (zato gubi "
            "od unigrama), interpolacija pobjeđuje.",
    "q5_1": "Nadzirano = imaš točne odgovore. Vreća riječi = svaka riječ jedna značajka, redoslijed ide u smeće. "
            "Sljedeća riječ = klasifikacija s |V| razreda.",
    "q5_2": "`z = w·x + b` skupi dokaze, sigmoid ih stisne u (0, 1). Pozitivna težina = glas za razred 1. "
            "Softmax = sigmoid za više razreda.",
    "q5_3": "Gubitak kaže koliko griješiš, gradijent kamo ići. Korak = η · (ŷ − y) · x. SGD se popravlja nakon "
            "svakog primjera; epoha = jedan krug.",
    "q5_4": "Točnost laže kad su razredi neuravnoteženi. P = pogođeni među izabranima, R = pronađeni među "
            "traženima, F1 = njihova harmonijska sredina.",
    "q5_5": "Težine pokazuju što je model naučio, ponekad i gluposti (prečaci). Kartica modela = upute za uporabu "
            "i popis nuspojava.",
    "q6_1": "Reci mi s kim se družiš i reći ću ti tko si (Firth). Sličnost ≠ povezanost: kava–čaj nasuprot "
            "kava–šalica.",
    "q6_2": "Broji susjede, uspoređuj <b>kut</b> (kosinus), ne duljinu. PPMI pita »češće nego slučajno?« i tako "
            "utiša zarez i »je«.",
    "q6_3": "tf = koliko u dokumentu (logaritmirano), idf = koliko rijetko u zbirci. Riječ u svim dokumentima ima "
            "idf 0. LSA spaja riječi u teme.",
    "q6_4": "Gusti vektori = kratki i pametni. Skip-gram pita »jesu li ovo susjedi?« uz nasumične protuprimjere. "
            "fastText slaže riječ od komadića, idealno za hrvatski.",
    "q6_5": "kralj − muškarac + žena ≈ kraljica (na velikom korpusu). Ugradnje upijaju i predrasude iz teksta. "
            "Vanjsko vrednovanje = pravi zadatak.",
}
