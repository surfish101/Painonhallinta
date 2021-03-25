# Modulin funktioilla lasketaan  painoindeksi (BMI) ja kehon rasvaprosentti

# Funktioiden määrittelyt

# Painoindeksi
def bmi(paino, pituus):
    """ Laskee painoindeksin kaavalla paino/(pituus/100)^2

    Args:
        paino (float): Paino kilogrammoina (kg)
        pituus (float): Pituus senttimetreinä (cm)

    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / (pituus/100)**2
    return painoindeksi

# Rasvaprosentti
def rasvaprosentti(bmi, ika, sukupuoli):
    """ Laskee henkilön rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): ikä vuosina
        sukupuoli (float): 1 - Miehet, 0 - Naiset

    Returns:
        float: kehon rasvaprosentti
    """
    # Aikuisen rasvaprosentti
    if ika >= 18:
        rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    else:
        # Lapsen rasvaprosentti
        rprosentti = 1.51 * bmi - 0.7 * ika - 3.6 * sukupuoli + 1.4

    return rprosentti

# Funktioiden testaukset
if __name__ == '__main__':

    # 1. Testataan painoindeksi
    pituus = 180
    paino = 100
    jokubmi = bmi(paino, pituus)
    print('Pituus:', pituus, 'Paino:', paino, 'Painoindeksi:', jokubmi)

    # 2. Testataan rasvaprosentti
    ika = 35
    sukupuoli = 1
    print('Rasvaprosentti:', rasvaprosentti(jokubmi, ika, sukupuoli))