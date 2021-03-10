# Tiivistetty versio Sanity.py-modulista eli suurinpiirtein se, mitä tuhosin vahingossa

def liukuluvuksi(syote):
    """Tarkistaa syötteen ja muuttaa sen liukuluvuksi

    Args:
        syote (string): Käyttäjän syöttämä arvo

    Returns:
        list: virhekoodi, virhesanoma ja syöte liukulukuna
    """

    # Asetetaan palautusarvojen oletukset
    virhekoodi = 0
    virhesanoma = 'Syöte OK'
    arvo = 0

    # Puhdistetaan syöte ylimääräisistä merkeistä (Whitespace)
    syote = syote.strip()

    # Selvitetään sisältääko syöte mahdollisen desimaalipilkun ja korvataan se pisteellä
    if syote.find(',') != -1:
        syote = syote.replace(',', '.')

    # Selvitetään sisältääkö syöte desimaalipisteen ja jaetaan syöte pisteen kohdalta useammaksi merkkijonoksi
    if syote.find('.') != -1:
        osat = syote.split('.')

        # Selvitetään onko osia enemmän kuin 2, eli onko useita pisteitä
        if len(osat) > 2:
            virhekoodi = 1
            virhesanoma = 'Syöte sisältää useita erottimia. Vain yksi arvo on sallittu'
            
        # Jos osia on 2
        else:
            osa = str(osat[0])  

            # Jos ensimmäinen osa on numeerinen ts. ei sisällä muita merkkejä kuin 0...9      
            if osa.isnumeric():
                osa = str(osat[1])

                # Jos toinenkin osa on numeerinen
                if osa.isnumeric():
                    arvo = float(syote)
                else:
                    virhekoodi = 4
                    virhesanoma =  'Desimaalierottimen jälkeen ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu'

            else:
                virhekoodi = 3
                virhesanoma = 'Ennen desimaalierotinta ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu'
                

    # Tarkistetaan onko desimaaliton syöte numeerista
    elif syote.isnumeric():
        arvo = float(syote)
    else:
        virhekoodi = 2
        virhesanoma = 'Syötteessä ylimäärisiä merkkejä: vain numerot ja desimaalipiste on sallittu'   
    
    # Muodostetaan funktion paluuarvo ja palautetaan se
    paluuarvo = [virhekoodi, virhesanoma, arvo]
    return paluuarvo


# Funktio, jolla tarkistetaan, että syötetty arvo on haluttujen rajojen sisällä
def rajatarkistus(arvo, alaraja, ylaraja):
    """Tarkistaa, että syötetty arvo on suurempi tai yhtäsuuri kuin alaraja ja pienempi tai yhtäsuuri kuin yläraja

    Args:
        arvo (float): tarkistettu arvo
        alaraja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo

    Returns:
        list: virhekoodi, virheilmoitus
    """

    virhekoodi = 0
    virhesanoma = 'Arvo ok'
    
    # Arvo alle alarajan
    if arvo <= alaraja:
        virhekoodi = 5
        virhesanoma = 'Annettu arvo alle alarajan (' + str(alaraja) + ').'

    # Arvo yli ylärajan
    if arvo >= ylaraja:
        virhekoodi = 6
        virhesanoma = 'Annettu arvo yli ylärajan (' + str(ylaraja) + ').'

    # Paluuarvon määritys ja palautus
    paluuarvo = [virhekoodi, virhesanoma]
    return paluuarvo

# Funktioiden testaus

if __name__ == '__main__':
    
    # 1. Syötteen tarkistus, syöte oikein
    syote = '123.5'
    print('Syöte:', syote, 'Tulokset:', liukuluvuksi(syote))

    # 2. Syötteessä desimaalipilkku, muuten oikein
    syote = '123,5'
    print('Syöte:', syote, 'Tulokset:', liukuluvuksi(syote))

    # 3. Syötteessä useampi desimaalipiste
    syote = '12.3.5'
    print('Syöte:', syote, 'Tulokset:', liukuluvuksi(syote))

    # 4. Syötteen alussa tekstiä
    syote = 'paino 70.5'
    print('Syöte:', syote, 'Tulokset:', liukuluvuksi(syote))

    # 5. Syötteen lopussa tekstiö
    syote = '80.5 kg'
    print('Syöte:', syote, 'Tulokset:', liukuluvuksi(syote))

    # 6.  Syöte pelkkää tekstiä
    syote = 'satakaksikymmentäkolme'
    print('Syöte:', syote, 'Tulokset:', liukuluvuksi(syote))
    
    
    # Rajatarkistukset
    alaraja = 30
    ylaraja = 300

    # 1. Rajojen sisällä
    arvo = 50
    print('Arvo:', arvo, 'Tulokset:', rajatarkistus(arvo, alaraja, ylaraja))

    # 2. Alle alarajan
    arvo = 25
    print('Arvo:', arvo, 'Tulokset:', rajatarkistus(arvo, alaraja, ylaraja))

    # 3. Yli ylärajan
    arvo = 350
    print('Arvo:', arvo, 'Tulokset:', rajatarkistus(arvo, alaraja, ylaraja))