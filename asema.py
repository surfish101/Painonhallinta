# Sääasema oliosovellus

class Weatherstation:
    """Yliluokka sääasemille"""
    def __init__(self, name, type, location):
        self.name = name
        self.type = type
        self.location = location

class Observation(Weatherstation):
    """Säähavainto aliluokka"""
    def __init__(self, date: str, temperature, windspeed, wind_direction, cloudcoverage, visibility):
        self.date = date
        self.temperature = str(temperature) +'\'c'
        self.windspeed = windspeed
        self.wind_direction = wind_direction
        self.cloudcoverage = cloudcoverage
        self.visibility = visibility

    def windspeed_kilometers(self):
        kmspeed = self.windspeed * 3.6
        return kmspeed

    def windspeed_knots(self):
        knotspeed = self.windspeed * 1.94
        return knotspeed


if __name__ == "__main__":

    turun_lentoasema = Weatherstation('Turun Lentoasema', 'Lentokenttä', 'Turku')
    isokari = Weatherstation('Isokarin sääasema', 'Rannikkoasema', 'Kustavi')

    havainto = Observation('24.03.2021', 5, 20, 300, 4/8, 3)

    print('Säähavainto tehtiin', havainto.date + ', lämpötila oli', havainto.temperature, "\nTuulennopeus oli:", str(havainto.windspeed) + 'm/s ja suunta', havainto.wind_direction, 'astetta')
    print(str(havainto.windspeed) + 'm/s kilometreinä tunnissa on', havainto.windspeed_kilometers())

    print('Tuulennopeus solmuissa oli', havainto.windspeed_knots())