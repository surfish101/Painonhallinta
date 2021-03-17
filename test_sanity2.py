# Sanity2-modulin testit

# Modulin lataus
import sanity2

#RAJA-ARVOTARKASTUSTEN TESTIT

# Arvo rajojen sisällä, virhekoodi 0, virhesanoma Arvo OK
def test_rajatarkistus_oikein():
    assert sanity2.rajatarkistus(100, 20, 300) == [0, 'Arvo OK']

# Arvo alle alarajan, virhekoodi 5, virhesanoma 'Annettu arvo alle alarajan (20).'
def test_rajatarkistus_alle():
    assert sanity2.rajatarkistus(10, 20, 300) == [5, 'Annettu arvo alle alarajan (20).']

# Arvo yli ylärajan, virhekoodi 6, virhesanoma 'Annettu arvo yli ylärajan (300).'
def test_rajatarkistus_yli():
    assert sanity2.rajatarkistus(350, 20, 300) == [6, 'Annettu arvo yli ylärajan (300).']

#LIUKULUKUMUUNNOSTESTIT

# 1. Syötteen tarkistus, syöte oikein; virhekoodi 0, virhesanoma 'Syöte OK', arvo 125.5
def test_liukuluvuksi_ok():
    assert sanity2.liukuluvuksi('125.5') == [0, 'Syöte OK', 125.5]

# 2. Syötteessä desimaalipilkku, muuten oikein; virhekoodi 0, virhesanoma 'Syöte OK', arvo 125.5
def test_liukuluvuksi_pilkku():
    assert sanity2.liukuluvuksi('125,5') == [0, 'Syöte OK', 125.5]

# 3. Syötteessä useampi desimaalipiste; virhekoodi 1, virhesanoma 'Syöte sisältää useita erottimia. Vain yksi arvo on sallittu', arvo 0
def test_liukuluvuksi_monta_pistetta():
    assert sanity2.liukuluvuksi('12.5.5') == [1, 'Syöte sisältää useita erottimia. Vain yksi arvo on sallittu', 0]

# 4. Syötteen alussa tekstiä; virhekoodi 3, virhesanoma 'Ennen desimaalierotinta ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu', arvo 0
def test_liukuluvuksi_teksti_ennen():
    assert sanity2.liukuluvuksi('paino 125.5') == [3, 'Ennen desimaalierotinta ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu', 0]

# 5. Syötteen lopussa tekstiä; virhekoodi 4, virhesanoma 'Desimaalierottimen jälkeen ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu', arvo 0
def test_liukuluvuksi_teksti_lopussa():
    assert sanity2.liukuluvuksi('125.5 kg') == [4, 'Desimaalierottimen jälkeen ylimääräisiä merkkejä: vain numerot ja desimaalipiste on sallittu', 0]

# 6.  Syöte pelkkää tekstiä; virhekoodi 2, virhesanoma 'Syötteessä ylimäärisiä merkkejä: vain numerot ja desimaalipiste on sallittu', arvo 0
def test_liukuluvuksi_teksti():
    assert sanity2.liukuluvuksi('sataviisi') == [2, 'Syötteessä ylimäärisiä merkkejä: vain numerot ja desimaalipiste on sallittu', 0]