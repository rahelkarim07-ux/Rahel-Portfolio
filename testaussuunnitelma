# Projektin testaussuunnitelma ja laadunvarmistus

Tässä dokumentissa määritellään projektin laatuvaatimukset, testausmenetelmät, testiympäristöt sekä yksityiskohtaiset testitapaukset.

---

## 1. Testausstrategia ja ympäristöt

* **Kohdesovellukset:**
  * Portfolion selainkäyttöliittymä (`index.html`, `style.css`)
  * Python CLI -sovellukset (`calculator.py`, `todo.py`)
* **Testatut selaimet:** Google Chrome, Mozilla Firefox, Microsoft Edge
* **Resoluutiot:** Desktop (1920x1080), Tabletti (768x1024), Mobiili (375x667 ja 390x844)
* **Python-versio:** Python 3.10+

---

## 2. Toiminnalliset testitapaukset

### A. Python Calculator (`calculator.py`)

| Testi ID | Testikohde | Toimenpide / Syöte | Odotettu lopputulos | Tila |
|---|---|---|---|---|
| **CALC-01** | Peruslaskut | Suorita yhteen-, vähennys-, kerto- ja jakolaskuja | Oikeat matemaattiset tulokset | Hyväksytty |
| **CALC-02** | Nollalla jako | Yritä jakaa mikä tahansa luku nollalla (`x / 0`) | Hallittu virheilmoitus ilman ohjelman kaatumista | Hyväksytty |
| **CALC-03** | Virheellinen syöte | Syötä kirjaimia tai erikoismerkkejä lukukenttään | Selkeä virheilmoitus ja uusi syöttömahdollisuus | Hyväksytty |

### B. Python To-Do CLI (`todo.py`)

| Testi ID | Testikohde | Toimenpide / Syöte | Odotettu lopputulos | Tila |
|---|---|---|---|---|
| **TODO-01** | Tehtävän lisäys | Lisää uusi tehtävä listaan | Tehtävä tallentuu ja näkyy uniikilla tunnisteella | Hyväksytty |
| **TODO-02** | Tehtävän kuittaus | Merkitse tehtävä valmiiksi tunnisteen perusteella | Tehtävän tila päivittyy valmiiksi | Hyväksytty |
| **TODO-03** | Tyhjä syöte | Yritä lisätä tehtävä ilman nimeä (pelkkä Enter) | Ohjelma estää tyhjän lisäyksen ja varoittaa käyttäjää | Hyväksytty |

### C. Selainportfolio (`index.html` & `style.css`)

| Testi ID | Testikohde | Toimenpide / Syöte | Odotettu lopputulos | Tila |
|---|---|---|---|---|
| **WEB-01** | Linkkien toimivuus | Klikkaa projektilinkkejä ja ulkoisia linkkejä | Kaikki linkit avautuvat oikein ilman 404-virheitä | Hyväksytty |
| **WEB-02** | Responsiivisuus | Pienennä näytön leveys alle 768 px | Ulkoasu mukautuu mobiiliin, ei sivuttaisskrollausta | Hyväksytty |
| **WEB-03** | Resurssien lataus | Tarkista kuvien ja tyylitiedostojen latautuminen | Kaikki grafiikat ja tyylit latautuvat (HTTP 200) | Hyväksytty |
