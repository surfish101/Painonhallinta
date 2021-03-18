# Tämä on painonhallintasovelluksen pääohjelma

# Kirjastojen ja modulien käyttöönotot
import sanity2
import laskenta

# Varsinaisen pääohjelman alku

# Komponenttien alustukset

# Työsilmukka. Ikuinen silmukka jossa on poistumistoiminto
uusi = 'K'
while True:
    
    # Kysytään käyttäjältä paino
    tapahtui_virhe = True

    # Silmukka jossa pyöritään kunnes saadaan painolle järkevä arvo
    while tapahtui_virhe == True:
        paino_str = input('Paino kilogrammoina: ')
        tulokset = sanity2.liukuluvuksi(paino_str)
        
        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:
            paino = tulokset[2]
            tarkistettu_paino = sanity2.rajatarkistus(paino, 40, 300)

            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_paino[0] == 0:
                tapahtui_virhe = False
            else:
                # Tulostetaan virheilmoitus
                print(tarkistettu_paino[1])

        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus        
        else:
            print(tulokset[1])

    tapahtui_virhe = True
    # Silmukka jossa pyöritään kunnes saadaan pituudelle järkevä arvo
    while tapahtui_virhe == True:
        pituus_str = input('Pituus sentteinä: ')
        tulokset = sanity2.liukuluvuksi(pituus_str)

        if tulokset[0] == 0:
            pituus = tulokset[2]
            tarkistettu_pituus = sanity2.rajatarkistus(pituus, 100, 300)

            if tarkistettu_pituus[0] == 0:
                tapahtui_virhe = False
            else:
                print(tarkistettu_pituus[1])

        else:
            print(tulokset[1])
    
    tapahtui_virhe = True 
    # Silmukka jossa pyöritään kunnes saadaan pituudelle järkevä arvo
    while tapahtui_virhe == True:
        ika_str = input('Ikä vuosina: ')
        tulokset = sanity2.liukuluvuksi(ika_str)

        if tulokset[0] == 0:
            ika = tulokset[2]
            tarkistettu_ika = sanity2.rajatarkistus(ika, 3, 120)

            if tarkistettu_ika[0] == 0:
                tapahtui_virhe = False
            else:
                print(tarkistettu_ika[1])

        else:
            print(tulokset[1])
    
    tapahtui_virhe = True
    # Silmukka jossa pyöritään kunnes saadaan sukupuolelle järkevä arvo
    while tapahtui_virhe == True:
        sukupuoli_str = input('Käyttäjän sukupuoli: Nainen: 0, mies: 1: ')
        tulokset = sanity2.liukuluvuksi(sukupuoli_str)

        if tulokset[0] == 0:
            sukupuoli = tulokset[2]
            tarkistettu_sukupuoli = sanity2.rajatarkistus(sukupuoli, 0, 1)

            if tarkistettu_sukupuoli[0] == 0:
                tapahtui_virhe = False
            else:
                print(tarkistettu_sukupuoli[1])
        else:
            print(tulokset[1])
    
    # Lasketaan ja tulostetaan painoindeksi kahden desimaalin tarkkuudella
    kayttajan_painoindeksi = laskenta.bmi(paino, pituus)
    print('Painoindeksisi on:', str(round(kayttajan_painoindeksi, 2)))

    # Lasketaan ja tulostetaan rasvaprosentti kahden desimaalin tarkkuudella
    kayttajan_rasvaprosentti = laskenta.rasvaprosentti(kayttajan_painoindeksi, ika, sukupuoli)
    print('Rasvaprosenttisi on:', str(round(kayttajan_rasvaprosentti, 2)))
    
    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/e) ')
    if uusi.upper() == 'E':
        break