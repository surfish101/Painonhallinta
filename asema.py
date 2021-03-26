# Sääasema oliosovellus

class Saaasema:
    def __init__(self, nimi, tyyppi, sijainti, numero):
        self.nimi = nimi
        self.tyyppi = tyyppi
        self.sijainti = sijainti
        self.numero = numero

class Saahavainto(Saaasema):
    def __init__(self, numero, paivamaara: str, lampotila, tnopeus, tsuunta, pilvisyys, nakyvyys):
        super().__init__(numero)
        self.paivamaara = paivamaara
        self.lampotila = str(lampotila) +'\'c'
        self.tnopeus = tnopeus
        self.tsuunta = tsuunta
        self.pilvisyys = pilvisyys
        self.nakyvyys = nakyvyys

    def tnopeuskm(self):
        kmspeed = self.windspeed * 3.6
        return kmspeed

    def tnopeussolmu(self):
        knotspeed = self.windspeed * 1.94
        return knotspeed


if __name__ == "__main__":

    turun_lentoasema = Saaasema('Turun Lentoasema', 'Lentokenttä', 'Turku')
    isokari = Saaasema('Isokarin sääasema', 'Rannikkoasema', 'Kustavi')

    havainto = Saahavainto('24.03.2021', 5, 20, 300, 4/8, 3)

    print('Säähavainto tehtiin', havainto.paivamaara + ', lämpötila oli', havainto.lampotila, "\nTuulennopeus oli:", str(havainto.tnopeus) + 'm/s ja suunta', havainto.wind_direction, 'astetta')
    print(str(havainto.tnopeus) + 'm/s kilometreinä tunnissa on', havainto.tnopeuskm())

    print('Tuulennopeus solmuissa oli', havainto.tnopeussolmu())