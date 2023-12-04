class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Virheellinen kapasiteetti")
        
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Virheellinen kasvatuskoko")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def _tarkista_tila(self):
        if self.alkioiden_lkm == len(self.ljono):
            uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            uusi_lista[:len(self.ljono)] = self.ljono
            self.ljono = uusi_lista

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self._tarkista_tila()
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False

    def poista(self, n):
        if self.kuuluu(n):
            indeksi = self.ljono.index(n)
            self.ljono[indeksi:self.alkioiden_lkm - 1] = self.ljono[indeksi + 1:self.alkioiden_lkm]
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        uusi_joukko = IntJoukko()
        for alkio in a.to_int_list() + b.to_int_list():
            uusi_joukko.lisaa(alkio)
        return uusi_joukko

    @staticmethod
    def leikkaus(a, b):
        uusi_joukko = IntJoukko()
        for alkio in a.to_int_list():
            if b.kuuluu(alkio):
                uusi_joukko.lisaa(alkio)
        return uusi_joukko

    @staticmethod
    def erotus(a, b):
        uusi_joukko = IntJoukko()
        for alkio in a.to_int_list():
            if not b.kuuluu(alkio):
                uusi_joukko.lisaa(alkio)
        return uusi_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            return "{" + ", ".join(str(self.ljono[i]) for i in range(self.alkioiden_lkm)) + "}"
