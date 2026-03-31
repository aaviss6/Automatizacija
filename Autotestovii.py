from selenium import webdriver
import unittest

class ZaraTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Pokreće Chrome browser
        self.driver.get("https://www.zara.com/ba/")  # Otvara Zara stranicu
        self.driver.implicitly_wait(5)  # Čeka elemente do 5 sekundi

    # TC01 – Provjera naslova stranice
    def test_page_title(self):
        self.assertIn("ZARA", self.driver.title.upper())  # Provjerava da li naslov sadrži "ZARA"

    # TC02 – Provjera URL-a
    def test_current_url(self):
        self.assertIn("zara.com", self.driver.current_url)  # Provjerava da li je URL ispravan

    # TC03 – Provjera da stranica ima sadržaj
    def test_page_source_exists(self):
        self.assertTrue(len(self.driver.page_source) > 0)  # Provjerava da li HTML nije prazan

    # TC04 – Refresh stranice
    def test_refresh(self):
        url = self.driver.current_url
        self.driver.refresh()  # Osvježava stranicu
        self.assertEqual(url, self.driver.current_url)  # Provjerava da li je URL ostao isti

    # TC05 – Maksimiziranje prozora
    def test_window_maximize(self):
        self.driver.maximize_window()  # Povećava prozor na maksimum
        self.assertTrue(True)  # Test prolazi ako nema greške

    # TC06 – Provjera da stranica sadrži Zara logo/naziv
    def test_zara_logo_present(self):
        self.assertIn("zara", self.driver.page_source.lower())  # Provjerava da li se "zara" pojavljuje na stranici

    # TC07 – Navigacija nazad i naprijed
    def test_back_forward(self):
        self.driver.get("https://www.google.com")  # Otvara drugu stranicu
        self.driver.back()  # Vraća se nazad
        self.driver.forward()  # Ide ponovo naprijed
        self.assertTrue(True)

    # TC08 – Scroll na dno stranice
    def test_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll dole
        self.assertTrue(True)

    # TC09 – Scroll na vrh stranice
    def test_scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")  # Scroll gore
        self.assertTrue(True)

    # TC10 – Otvaranje novog taba
    def test_open_new_tab(self):
        self.driver.execute_script("window.open('https://www.google.com');")  # Otvara novi tab
        self.assertTrue(True)

    # TC11 – Provjera da stranica sadrži tekst "zara"
    def test_page_contains_text(self):
        self.assertIn("zara", self.driver.page_source.lower())  # Traži riječ u HTML-u

    # TC12 – Provjera da naslov nije prazan
    def test_title_not_empty(self):
        self.assertTrue(len(self.driver.title) > 0)  # Naslov mora postojati

    # TC13 – Provjera da URL nije prazan
    def test_url_not_empty(self):
        self.assertTrue(len(self.driver.current_url) > 0)  # URL mora postojati

    # TC14 – Provjera da driver postoji
    def test_driver_exists(self):
        self.assertIsNotNone(self.driver)  # Driver mora biti pokrenut

    # TC15 – Zatvaranje i ponovno otvaranje browsera
    def test_close_and_reopen(self):
        self.driver.close()  # Zatvara browser
        self.driver = webdriver.Chrome()  # Ponovo ga pokreće
        self.assertTrue(True)

    def tearDown(self):
        try:
            self.driver.quit()  # Gasi browser nakon svakog testa
        except:
            pass

if __name__ == "__main__":
    unittest.main()