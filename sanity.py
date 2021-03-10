# Moduli syötteen oikeellisuuden (sanity) tarkistamiseen
"""Tarkistaa käyttäjän syötteen oikeellisuuden tarkistusfunktioiden avulla
"""


# Funktioiden määrittelyt
def on_jarkeva(syote, alaraja, ylaraja):
    """
    Puhdistaa merkkijonosta ylimääräiset tulostumattomat merkit ja välilyönnit
    sekä selvittää onko syötetty arvo annettujen rajojen sisällä. 
    Funktio muutta desimaali pilkun desimaalipisteeksi.


    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alarja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo

    Returns (float) : Käyttäjän syöttämä arvo numeerisena
    """

    # Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = syote.lstrip()

    #  Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = puhdistettu_syote.rstrip()

    # Selvitetään onko merkkijonossa pilkku (,)
    pilkunpaikka = puhdistettu_syote.find(',')

    # Jos pilkku löytyy, korvataan pisteellä
    if pilkunpaikka != -1:
        korjattu_syote = puhdistettu_syote.replace(',', '.')
    else:
      korjattu_syote = puhdistettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi
    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot sallittu')
        luku = 0
    # Tarkistetaan, ettei syöte ole alarajan alapuolella
    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)

    # Tarkistetaan, ettei syöte ole ylärajan yläpuolella
    try:
        if luku > ylaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
        print(virheilmoitus)
    
    # Palautetaan luku
    return luku

def liukuluku_ok(syote, alaraja, ylaraja):
    """Tarkistaa syötteen olevan numeerinen ja muuttaa sen liukuluvuksi. Syötteellä on alaraja ja yläraja
    
    Args:
        syote (string): Syötteenä saatu arvo
        alaraja (float): pienin hyväksyttävä arvo
        ylaraja (float): suurin hyväksyttävä arvo

    Returns:
        list: Palauttaa arvon (float), virhekoodin (int), virhesanoman (string)
    """
    # Puhdistetaan syötteestä ylimääriset merkit (white space)
    puhdistettumerkkijono = syote.strip()

    # Tutkitaan onko syötteessä pilkku ja etsitään sen paikka
    pilkunpaikka = puhdistettumerkkijono.find(',')

    # Jos pilkku löytyi, korvataan pisteellä
    if pilkunpaikka != -1: # Jos ei löydy indeksi on aina -1
        numeroarvo = puhdistettumerkkijono.replace(',', '.') # Muutetaan
    else:
        numeroarvo = puhdistettumerkkijono # ei muuteta

    # Etsitään desimaalipistettä merkkijonosta
    pisteenpaikka = numeroarvo.find('.')

    # Jos desimaalipiste löytyy, jaetaan pisteen kohdalta erillisiksi merkkijoiksi
    if pisteenpaikka != -1:
        osat = numeroarvo.split('.') # Syntyy lista osista
        osien_maara = len(osat)
        # Selvitetään onko osia enemmän kuin 2 so. liikaa pilkkuja tai pisteitä
        if osien_maara > 2:
            virhekoodi = 1
            virhesanoma = "Syötteessä on useita desimaalipisteitä tai useita arvoja: vain yksi liukuluku on sallittu, esim 12.3"
            arvo = 0

        # Muussa tapauksessa selvitetään onko alkuosassa pelkkiä numeroita
        else:
            osa = str(osat[0])
            if osa.isnumeric() == False:
                virhekoodi = 2
                virhesanoma = "Syöte sisältää tekstiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim. 123.5"
                arvo = 0
            # Selvitetään onko loppuosassa pelkkiä numeroita    
            else:
                osa = str(osat[1])
                if osa.isnumeric() == False:
                    virhekoodi = 2
                    virhesanoma = "Syöte sisältää tekstiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim. 123.5"
                    arvo = 0
                # Jos ei ollut asetetaan arvo ja nollataan virheilmoitukset
                else:
                    virhekoodi = 0
                    virhesanoma = "Syöte OK"
                    arvo = float(numeroarvo)
    # Jos yksiosainen syöte sisältää muutakin kuin pelkkiä numeroita
    elif numeroarvo.isnumeric() == False:
        virhekoodi = 2
        virhesanoma = "Syöte sisältää tekstiä, ainoastaan numerot ja desimaalipiste ovat sallittuja, esim. 123.5"
        arvo = 0

    # Yksiosainen syöte OK
    else:    
        virhekoodi = 0
        virhesanoma = "Syöte OK"
        arvo = float(numeroarvo)

    # TODO: Muodosta kaksi funktiota: float-tarkistus ja raja-arvotarkistus erillisinä funktioina
                    
    # Muodostetaan ja palautetaan funktion paluuarvo (lista)        
    tulokset = [virhekoodi, virhesanoma, arvo]
    return tulokset
    
# Jos sanity.py-tiedostoa ajetaan terminaalissa, suoritetaan testit
if __name__ == '__main__':
    
#     Testataan toimintaa
#     tulos = on_jarkeva('sata', 1, 500)
#     print(tulos)
#     syote = ' 10.5   '
#     print(syote.strip(), 'kiloa')

    # Testataan 
    syote = 'sata'
    print(liukuluku_ok(syote, 0, 500))