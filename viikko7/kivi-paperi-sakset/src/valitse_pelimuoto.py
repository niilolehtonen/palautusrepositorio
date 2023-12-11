from kps_pelaaja_vs_pelaaja import KPSPelaajaVSPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class ValitsePelimuoto():
    def __init__(self,vastaus):
        self._vastaus = vastaus
    
    def valitse_pelimuoto(self):
        if self._vastaus == "a":
            kps_pvp = KPSPelaajaVSPelaaja()
            kps_pvp.pelaa()
        elif self._vastaus == "b":
            kps_yksinpeli = KPSTekoaly()
            kps_yksinpeli.pelaa()
        elif self._vastaus == "c":
            kps_yksinpeli_haastavampi = KPSParempiTekoaly()
            kps_yksinpeli_haastavampi.pelaa()

        return None