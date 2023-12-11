from valitse_pelimuoto import ValitsePelimuoto

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s2")
        kps = ValitsePelimuoto(vastaus)
        if kps.valitse_pelimuoto() == None:
            break
        kps.valitse_pelimuoto()



if __name__ == "__main__":
    main()
