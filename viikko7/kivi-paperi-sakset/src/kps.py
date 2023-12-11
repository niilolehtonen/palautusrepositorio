from tuomari import Tuomari

class KiviPaperiSakset:
    def __init__(self):
        self.ekan_siirto = None
        self.tokan_siirto = None

    def pelaa(self):
        tuomari = Tuomari()

        self._ekan_siirto = self._ensimmaisen_siirto()
        self._tokan_siirto = self._toisen_siirto(self._ekan_siirto)

        while self._onko_ok_siirto(self._ekan_siirto) and self._onko_ok_siirto(self._tokan_siirto):
            tuomari.kirjaa_siirto(self._ekan_siirto, self._tokan_siirto)
            print(tuomari)

            self._ekan_siirto = self._ensimmaisen_siirto()
            self._tokan_siirto = self._toisen_siirto(self._ekan_siirto)


        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"