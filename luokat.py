# Tässä modulissa määritellään luokat painonhallintasovellukseen

# Modulien ja kirjastojen lataukset

# Henkilö-luokka

class Henkilo:
    """Yliluokka kaikille henkilötyypeille"""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):
        
        self.etunimi = etunimi
        self.sukunimi = sukunimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

    def painoindeksi(self):
        bmi = self.paino / (self.pituus / 100) ** 2
        return bmi

    @staticmethod
    def bmi(pituus, paino):
        bmi = paino / (pituus/100)**2
        return bmi

class Aikuinen(Henkilo):
    """Aliluokka aikuiselle henkilölle, perii Henkilo-luokan ominaisuudet ja metodit"""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        self.tavoitepaino = tavoitepaino
        
    def rasvaprosentti(self):
        rasvaprosentti = 1.2 * self.painoindeksi() + 0.23 * self.ika - 10.8 * self.sukupuoli - 5.4
        return rasvaprosentti

class Lapsi(Henkilo):
    """Aliluokka lapselle, perii Henkilo-luokan ominaisuudet ja metodit"""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
    
    def rasvaprosentti(self):
        rasvaprosentti = 1.51 * self.painoindeksi() - 0.7 * self.ika - 3.6 * self.sukupuoli + 1.4
        return rasvaprosentti
        

if __name__ == "__main__":
    mikaV = Henkilo('Mika', 'Vainio', 171, 74, 59, 1)
    print(mikaV.etunimi, 'painaa', mikaV.paino, 'kiloa')

    mikaV.painoindeksi()

    mikaV2 = Aikuinen('Mika', 'Vainio', 171, 74, 59, 1, 70)
    print(mikaV2.etunimi + 'n', 'painoindeksi on', mikaV2.painoindeksi())
    print(mikaV2.etunimi + 'n', 'rasvaprosentti on', mikaV2.rasvaprosentti())

    # Lasketaan painoindeksi staattisella metodilla
    pituus = 171
    paino = 74
    
    print('Painoindeksi on', Henkilo.bmi(pituus, paino))