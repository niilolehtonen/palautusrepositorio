from kps import KiviPaperiSakset

class KPSPelaajaVSPelaaja(KiviPaperiSakset):
    
    def _toisen_siirto(self, ensimmäisen_siirto):
        return input("Toisen pelaajan siirto: ")
