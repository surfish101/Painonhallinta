# Rutiineja tietojen kysymiseen käyttäjältä

# Kirjastojen & moduulien lataukset
import sanity2

# Funktioiden määrittelyt

def kysy_liukuluku(kysymys, alaraja, ylaraja):
    """Kysyy käyttäjältä liukuluvun tai kokonaisluvun ja tarkistaa syötteen oikean tietotyypin ja suuruuden

    Args:
        kysymys (string): Käyttäjälle esitettävä kysymys
        alaraja (float): Pienin sallittu arvo
        ylaraja (float): Suurin sallittu arvo

    Returns:
        float: Käyttäjän syöttämä arvo liukulukuna
    """
    # Kysytään käyttäjältä tietoa kunnes saadaan järkevä arvo
    luku = 0
    tapahtui_virhe = True

    while tapahtui_virhe == True:
        vastaus_str = input(kysymys)
        tulokset = sanity2.liukuluvuksi(vastaus_str)
        
        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:
            vastaus = tulokset[2]
            tarkistettu_vastaus = sanity2.rajatarkistus(vastaus, alaraja, ylaraja)

            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_vastaus[0] == 0:
                tapahtui_virhe = False
                luku = vastaus
                
            else:
                # Tulostetaan virheilmoitus
                print(tarkistettu_vastaus[1])

        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus        
        else:
            print(tulokset[1])

    return luku

if __name__ == '__main__':
    vastaus = kysy_liukuluku('Anna luku', 100, 200)
    print(vastaus)