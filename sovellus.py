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

    # Silmukka jossa pyöritään kunnes saadaan järkevä arvo
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
    # Kysytään käyttäjältä pituus
    while tapahtui_virhe == True:
        pituus_str = input('Pituus metreinä: ')
        tulokset = sanity2.liukuluvuksi(pituus_str)

        if tulokset[0] == 0:
            pituus = tulokset[2]
            tarkistettu_pituus = sanity2.rajatarkistus(pituus, 1.0, 3.0)

            if tarkistettu_pituus[0] == 0:
                tapahtui_virhe = False
            else:
                print(tarkistettu_pituus[1])

        else:
            print(tulokset[1])
    
    tapahtui_virhe = True 
    # Kysytään käyttäjän ikä
    while tapahtui_virhe == True:
        ika_str = input('Ikä vuosina: ')
        tulokset = sanity2.liukuluvuksi(ika_str)

        if tulokset[0] == 0:
            ika = tulokset[2]
            tarkistettu_ika = sanity2.rajatarkistus(ika, 18, 100)

            if tarkistettu_ika[0] == 0:
                tapahtui_virhe = False
            else:
                print(tarkistettu_ika[1])

        else:
            print(tulokset[1])
    '''
    tapahtui_virhe = True
    # Kysytään käyttäjältä sukupuoli
    while tapahtui_virhe == True:
        sukupuoli_str = input('Nainen 0, mies 1: ')
        tulokset = sanity2.liukuluvuksi(sukupuoli_str)

        if tulokset[0] == 0:
            sukupuoli = tulokset[2]
            tapahtui_virhe = False
        else:
            print(tulokset[1])
    '''

    
    # Poistuminen ikuisesta silmukasta
    uusi = input('Lasketaanko uuden henkilön rasvaprosentti? (K/E) ')
    if uusi == 'E' or uusi == 'e':
        break