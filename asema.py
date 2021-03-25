# Sääasema oliosovellus

class Weatherstation:
    """Yliluokka sääasemille"""
    def __init__(self, name, type, location):
        self.name = name
        self.type = type
        self.location = location

class Observation(Weatherstation):
    """Säähavainto aliluokka"""
    def __init__(self, name, type, location, date, temperature, windspeed, wind_direction, cloudcoverage, visibility):
        super().__init__(name, type, location)
        self.date = date
        self.temperature = temperature
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

    turun_lentoasema = Observation('Turun Lentoasema', 'lentokenttä', 'Turku', '25.03.2021', 6.0, 8.0, 180, '5/8', 5)
    print(turun_lentoasema.location, turun_lentoasema.temperature, 'C', 'Tuulen nopeus (km/h):', turun_lentoasema.windspeed_kilometers(), 'Tuulen nopeus solmuissa:', turun_lentoasema.windspeed_knots())