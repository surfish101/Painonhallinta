# Modulin laskenta.py testit

# Modulien & kirjastojen lataukset
import laskenta

# Ensimmäinen testi lasketaan painoindeksi ja verrataan tulosta ennalta laskettuun arvoon
def test_painoindeksi():
    assert round(laskenta.bmi(74, 171), 2) == 25.31 # huom pöristys

# Pojan rasvaprosentti kun bmi on 25 ja ikä 13
def test_pojan_rasvaprosentti():
    assert round(laskenta.rasvaprosentti(25, 13, 1), 2) == 26.45 #huom pyöristys

# Tytön rasvaprosentti kun bmi on 25 ja ikä 16
def test_tyton_rasvaprosentti():
    assert round(laskenta.rasvaprosentti(25, 16, 0), 2) == 27.95 # huom pyöristys

# Aikuisen miehen rasvaprosentti kun bmi on 25 ja ikä 30
def test_miehen_rasvaprosentti():
    assert round(laskenta.rasvaprosentti(25, 30, 1), 2) == 20.70 # huom pyöristys

# Aikuisen naisen rasvaprosentti kun bmi on 25 ja ikä 45
def test_naisen_rasvaprosentti():
    assert round(laskenta.rasvaprosentti(25, 45, 0), 2) == 34.95 # huom pyöristys