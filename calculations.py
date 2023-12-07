import math

fahrenheit = float
celsius = float
rankine = float
kelvin = float
inHg = float
milliBar = float
hPa = milliBar
feet = float


# magnus coefficients
A = 17.625
B: celsius = celsius(243.04)


def dew_point(temperature:celsius, relative_humidity:float) -> celsius:
    x = math.log(relative_humidity/100) + (A*temperature) / (B+temperature)
    return celsius((B* x) / (A-x))

# I think this is introducing a slight difference than reality in here....
def vapor_pressure(dewpoint_temperature:celsius) -> float:
    return 6.11 * math.pow(10, (7.5*dewpoint_temperature)/(237.7+dewpoint_temperature))

def virtual_temperature(temperature:kelvin, vapor_pressure, station_pressure:milliBar) -> kelvin:
    return kelvin(temperature / ( 1 - (vapor_pressure / station_pressure) * (1-.622)))

def celsius_to_kelvin(temperature:celsius)->kelvin:
    return kelvin(temperature+273.16)

def kelvin_to_rankine(temperature:kelvin) -> rankine:
    return rankine( ( (9/5) * (temperature - 273.16) + 32 ) + 459.69 )

def hPa_to_inHg(pressure:hPa) -> inHg:
    return inHg(pressure * 0.02953)

def density_altitude(pressure:inHg, virtual_temperature:rankine) -> feet:
    x = (17.326 * pressure) / virtual_temperature
    return feet(145366 * ( 1 - pow(x, .235) ))

def density_altidude_from_sensors(temperature:celsius, rel_humidity:float, pressure:hPa):
    vapor_pressure_ = vapor_pressure(dew_point(temperature, rel_humidity))
    virtual_temperature_ = virtual_temperature(celsius_to_kelvin(temperature), vapor_pressure_, pressure)
    density_altitude_ = density_altitude(hPa_to_inHg(pressure), kelvin_to_rankine(virtual_temperature_))
    return density_altitude_

