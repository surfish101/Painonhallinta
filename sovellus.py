# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import kysymys
import laskenta
import luokat

# Varsinaisen pääohjelman alku

# Työsilmukka. Ikuinen silmukka jossa on poistumistoiminto
uusi = 'K'
lista = []
while True:
    
    # Tehdään kysymykset modulin kysymys.py funktiota käyttämällä
    etunimi = input('Anna etunimesi: ')
    sukunimi = input('Anna sukunimesi: ')
    paino = kysymys.kysy_liukuluku('Paino kiloina: ', 30, 300)
    pituus = kysymys.kysy_liukuluku('Pituus sentteinä: ', 100, 250)
    ika = kysymys.kysy_liukuluku('Ikä vuosina: ', 3, 120)
    sukupuoli = kysymys.kysy_liukuluku('Sukupuoli: Nainen 0, mies 1: ', 0, 1)

    # Luodaan oliot iästä riippuen  
    if ika >= 18:
        tavoitepaino = kysymys.kysy_liukuluku('Tavoitepainosi kiloissa: ', 30, 300)
        aikuinen = luokat.Aikuinen(etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino)
        lista.append(aikuinen)
    else:
        lapsi = luokat.Lapsi(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        lista.append(lapsi)
    '''# Lasketaan ja tulostetaan painoindeksi kahden desimaalin tarkkuudella
    kayttajan_painoindeksi = laskenta.bmi(paino, pituus)
    print('Painoindeksisi on:', str(round(kayttajan_painoindeksi, 1)))

    # Lasketaan ja tulostetaan rasvaprosentti kahden desimaalin tarkkuudella
    kayttajan_rasvaprosentti = laskenta.rasvaprosentti(kayttajan_painoindeksi, ika, sukupuoli)
    print('Rasvaprosenttisi on:', str(round(kayttajan_rasvaprosentti, 1)))'''

    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/e) ')
    if uusi.upper() == 'E':
        break

# Ikuisen silmukan jälkeen tulostetaan tietoja

# Otetaan listan ensimmäinen olio pois ja tulostetaan sen tietoja
eka = lista.pop(0)
print(eka.etunimi, eka.sukunimi, eka.rasvaprosentti())

# Jos listassa on enemmän kuin yksi olio, otetaan listan viimeinen olio pois ja tulostetaan sen tietoja
if len(lista) > 0:
    vika = lista.pop()
    print(vika.etunimi, vika.sukunimi, vika.rasvaprosentti())