# Testy automatyczne dla ProductStore (DemoBlaze)

Repozytorium zawiera testy automatyczne dla strony **ProductStore (DemoBlaze)**:
[https://www.demoblaze.com/index.html](https://www.demoblaze.com/index.html)
Testy są napisane w **Pythonie** z użyciem **Playwright** i **Pytest**, z raportowaniem w **Allure** i podejściem **Page Object Model (POM)**.

---

## 🛠 Technologie

* Python 3.11+
* Playwright
* Pytest
* Allure
* Page Object Model (POM) dla lepszej organizacji testów

---

## 📂 Struktura projektu

```
playwright-tests/
│
├── Tests/                         # Pliki z testami
│   ├── test_home.py               # np. walidacja listy produktów / kategorii
│   ├── test_login.py              # logowanie (signup/login)
│   ├── test_cart.py               # koszyk: dodawanie/usuwanie, suma
│   ├── test_order.py              # zakup: formularz "Place Order"
│
├── Pages/                         # Page Object Model
│   ├── basePage.py
│   ├── homePage.py                # kategorie, listing produktów, przejście do PDP
│   ├── productPage.py             # strona produktu (PDP), Add to cart
│   ├── cartPage.py                # koszyk + Place Order
│   ├── authModal.py               # logowanie/rejestracja w modalu
│
├── reports/                       # Raporty testów (opcjonalnie)
├── environment.yml
├── conftest.py                    # Globalne fixture i hooki
├── pytest.ini                     # Konfiguracja uruchamiania testów
└── README.md
```

---

## ⚡ Instalacja

1. Sklonuj repozytorium:

```bash
git clone <url-repozytorium>
cd playwright-tests
```

2. (Opcjonalnie) Aktywuj środowisko (przykład dla conda):

```bash
conda activate demoblaze-tests
```

3. Zainstaluj zależności:

```bash
conda env create -f environment.yml
```

4. Zainstaluj przeglądarki Playwright:

```bash
python -m playwright install
```

---

## 🚀 Uruchamianie testów

Uruchom wszystkie testy:

```bash
pytest
```

Uruchom testy w trybie szczegółowym:

```bash
pytest -v
```

Uruchom konkretny plik z testami:

```bash
pytest Tests/test_cart.py
```

Wygeneruj raport (przykład HTML lub Allure – zależnie od konfiguracji):

```bash
pytest --html=reports/report.html
```

---

## ⚙️ Konfiguracja testów

### `pytest.ini`

Przykładowa konfiguracja uruchamiania (wiele przeglądarek + trace przy błędzie):

```ini
[pytest]
addopts = --browser chromium --browser firefox --browser webkit --tracing=retain-on-failure
```

**Co daje ta konfiguracja:**

* testy lecą na Chromium/Firefox/WebKit,
* trace zapisuje się tylko dla testów, które poległy (łatwiejszy debug).

---

### `conftest.py`

`conftest.py` definiuje globalne fixture i hooki, np.:

* tworzenie `page`/`context`,
* ustawienie bazowego URL: `https://www.demoblaze.com/index.html`,
* automatyczny screenshot po failu + załączenie do raportu Allure,
* (opcjonalnie) przełączniki typu `--headed`, `--slowmo`.

---

## 🧪 Co warto testować na DemoBlaze (propozycje)

**Opcja A: “Smoke” (szybko i stabilnie)**

* wejście na stronę, widoczność listy produktów,
* przejście do produktu (PDP),
* dodanie do koszyka,
* otwarcie koszyka i weryfikacja pozycji.

**Opcja B: “Auth + Cart” (więcej logiki)**

* signup / login w modalu,
* dodanie/usunięcie produktów w koszyku,
* weryfikacja sumy/ilości,
* poprawne komunikaty i stany UI.

**Opcja C: “E2E zakup” (najpełniejsze, ale bardziej kruche)**

* dodanie produktu do koszyka,
* “Place Order” → uzupełnienie formularza,
* finalizacja i weryfikacja potwierdzenia.

---

## 📝 Przykładowy test (ProductStore)

```python
from playwright.sync_api import expect

def test_add_product_to_cart(page, home_page, product_page, cart_page):
    home_page.navigate()
    home_page.open_product_by_name("Samsung galaxy s6")

    product_page.add_to_cart()
    product_page.accept_alert()

    cart_page.navigate()
    expect(cart_page.get_product_names()).to_contain_text(["Samsung galaxy s6"])
```

---

## 💡 Podsumowanie

Dzięki tej konfiguracji:

* testy są uporządkowane przez POM (czytelniej i łatwiej utrzymać),
* po błędach automatycznie masz screenshoty i trace,
* testy uruchamiasz na wielu przeglądarkach jednym poleceniem.