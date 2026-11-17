# Računalno jezikoslovlje (I051): priprema za kolokvije 🧠

Studentski materijali za **1. kolokvij** iz kolegija *Računalno jezikoslovlje* (teme P2–P7): odgovori na teorijska pitanja, interaktivni kviz, probni kolokvij i objašnjena rješenja pripreme za kolokvij. Svi brojevi u PDF-ovima dolaze iz programa u ovom repozitoriju, koji provjeravaju sami sebe.

> ⚠️ Odgovori, kviz i rješenja nisu službeni materijali. Ako nađeš grešku, otvori issue ili javi. Materijali profesora (predavanja, pitanja, bilježnica) nalaze se u mapi `materijali_profesora/`.

## 📄 PDF-ovi (mapa `pdf/`)

| datoteka | što je unutra | interaktivno |
|---|---|---|
| [`1_teorija_odgovori.pdf`](pdf/1_teorija_odgovori.pdf) | svih **30 teorijskih pitanja** (P2–P7) s odgovorima; uz svako pitanje žuti okvir **»ukratko«** za brzo ponavljanje; šalabahter formula | klikabilni sadržaj i knjižne oznake, kvačica »naučeno« uz svako pitanje, polje za bilješke po temi |
| [`2_kviz_i_probni_kolokvij.pdf`](pdf/2_kviz_i_probni_kolokvij.pdf) | **kviz od 30 pitanja** s ponuđenim odgovorima (5 po temi) i **probni kolokvij** od 5 novih zadataka s rješenjima | klikneš odgovor → »Točno!« s objašnjenjem ili pomoć i »pokušaj ponovno«; mapa pitanja; kvačice »iz prve« |
| [`3_kolokvij1_rjesenja.pdf`](pdf/3_kolokvij1_rjesenja.pdf) | samo **5 zadataka iz `kolokvij_1_priprema.ipynb`**: model-odgovor na teoriju, objašnjenje korak po korak, kod i stvarni ispis | klikabilni sadržaj, kvačica »riješeno« |

Kviz radi običnim poveznicama (bez JavaScripta), pa radi u svakom pregledniku PDF-a. Kvačice i bilješke ostaju zapamćene kad spremiš PDF (Ctrl+S); rade u Edgeu, Chromeu, Firefoxu i Adobe Readeru.

## 📂 Materijali profesora (mapa `materijali_profesora/`)

| datoteka | sadržaj |
|---|---|
| `predavanja/P1 Uvod.pdf` … `P7 Vektorska semantika i ugradnje 2027.pdf` | slajdovi predavanja P1–P7 |
| `kolokvij_1_pitanja.docx` | popis teorijskih pitanja za 1. kolokvij (na njih odgovara `1_teorija_odgovori.pdf`) |
| `kolokvij_1_priprema.ipynb` | bilježnica s 5 zadataka za pripremu (objašnjena u `3_kolokvij1_rjesenja.pdf`) |
| `links to github.pdf` | poveznice na profesorov GitHub s vježbama |

## 🐍 Programi (mapa `programi/`)

| datoteka | sadržaj |
|---|---|
| `zadatak1_rijeci_bpe.py` … `zadatak5_vektori.py` | rješenja 5 zadataka iz pripreme za kolokvij |
| `teorija_p2_unicode_bpe.py` … `teorija_p7_ugradnje.py` | primjeri za teoriju, jedan program po predavanju (UTF-8, regex, ELIZA, automat, tablica D, perpleksija, softmax, PMI, tf-idf, skip-gram …) |
| `probni_kolokvij.py` | rješenja probnog kolokvija |

Svaki program na kraju ima `assert` provjere: ako se ne pojavi `AssertionError`, rezultati se slažu s predavanjima i bilježnicom.

### Pokretanje

```bash
pip install -r requirements.txt
cd programi
python zadatak1_rijeci_bpe.py
```

**VS Code:** File → Open Folder → ova mapa → `Ctrl+Shift+P` → *Python: Select Interpreter* → otvori `.py` datoteku → ▶ *Run Python File*. Za bilježnice (`.ipynb`) instaliraj ekstenzije **Python** i **Jupyter**, pa *Select Kernel* → Python → *Run All*.

Ako se č, ć, đ … u Windows terminalu prikazuju krivo: `$env:PYTHONIOENCODING="utf-8"` (PowerShell).

## 🔧 Ponovna izrada PDF-ova

```bash
python izrada/napravi_pdfove.py
```

Skripta pokrene sve programe (pada ako neki `assert` ne prođe), u PDF upiše njihov stvarni ispis i izradi sva tri PDF-a u `pdf/`.

| datoteka u `izrada/` | sadržaj |
|---|---|
| `sadrzaj_teorija.py` | odgovori na 30 pitanja i formule |
| `sadrzaj_ukratko.py` | uvodi u teme i okviri »ukratko« |
| `sadrzaj_kolokvij1.py` | tekstovi, model-odgovori i objašnjenja zadataka kolokvija 1 |
| `sadrzaj_kviz.py` | pitanja kviza i probni kolokvij |
| `zajednicko.py`, `napravi_pdfove.py` | izgled i izrada PDF-ova (reportlab) |

Napomena: skripta koristi Windowsove fontove (Arial, Consolas, Segoe UI Symbol iz `C:\Windows\Fonts`). Na Linuxu/macOS-u treba promijeniti putanje u `izrada/zajednicko.py`.

## 📚 Izvori

- Vježbe (V02–V07) i materijali za kolokvij: <https://github.com/dseverdi/CL> ([mapa kolokvij](https://github.com/dseverdi/CL/tree/main/kolokvij): `kolokvij_1_pitanja.docx`, `kolokvij_1_priprema.ipynb`)
- Predavanja P1–P7 s kolegija (`materijali_profesora/predavanja/`; primjeri na korpusu UD Croatian SET)
- Jurafsky & Martin, *Speech and Language Processing*, 3. izd. (nacrt 2026.), pogl. 2–5 i 11

Sretno na kolokviju! 🍀
