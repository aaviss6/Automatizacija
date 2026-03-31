# Automatizacija

# Zara Web Tests

Ovaj projekAt sadrži automatske testove za web stranicu [Zara Bosna i Hercegovina](https://www.zara.com/ba/) koristeći Selenium i unittest framework u Pythonu.

## Sadržaj testova

Testovi pokrivaju osnovne funkcionalnosti stranice, uključujući:

1. Provjeru naslova stranice
2. Provjeru URL-a
3. Provjeru da stranica ima sadržaj
4. Osvježavanje stranice
5. Maksimiziranje prozora
6. Provjeru da stranica sadrži Zara logo/naziv
7. Navigaciju nazad i naprijed
8. Scrollanje na dno i vrh stranice
9. Otvaranje novog taba
10. Provjeru prisutnosti teksta "zara"
11. Provjeru da naslov i URL nisu prazni
12. Provjeru da driver postoji
13. Zatvaranje i ponovno otvaranje browsera

## Preduvjeti

- Python 3.8 ili noviji
- Google Chrome instaliran
- `webdriver-manager` za automatsko upravljanje Chromedriverom (nije potrebno ručno preuzimanje)

## Instalacija

1. Kopirajte ili preuzmite projekt.
2. Napravite virtualno okruženje (preporučeno):

```bash
python -m venv venv
# Aktivacija:
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
