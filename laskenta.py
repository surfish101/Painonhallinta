# Modulin funktioilla lasketaan  painoindeksi (BMI) ja kehon rasvaprosentti

# Funktioiden määrittelyt

# Painoindeksi
def bmi(paino, pituus):
    """ Laskee painoindeksin kaavalla paino/pituus^2

    Args:
        paino (float): Paino kilogrammoina
        pituus (float): Pituus metreinä

    Returns:
        float: painoindeksi
    """
    painoindeksi = paino / pituus**2
    return painoindeksi

# Aikuisen rasvaprosentti
def rasvaprosentti(bmi, ika, sukupuoli):
    """ Laskee rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): ikä
        sukupuoli (float): ikä

    Returns:
        float: kehon rasvaprosentti
    """
    rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    return rprosentti

# Funktioiden testaukset
if __name__ == '__main__':

    # 1. Testataan painoindeksi
    pituus = 1.8
    paino = 100
    jokubmi = bmi(paino, pituus)
    print('Pituus:', pituus, 'Paino:', paino, 'Painoindeksi:', jokubmi)

    # 2. Testataan rasvaprosentti
    ika = 35
    sukupuoli = 1
    print('Rasvaprosentti:', rasvaprosentti(jokubmi, ika, sukupuoli))