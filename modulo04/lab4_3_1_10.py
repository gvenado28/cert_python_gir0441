''''
Descripción: Programa que hará varios tipos de conversiones (m/km, l/gal, etc.).
Autor: German Venado
Fecha: 06 oct 2022
'''

def liters_100km_to_miles_gallon(liters):
    galon = liters / 3.785411784
    milla = 100 * 1000 / 1609.344
    return milla / galon
    
def miles_gallon_to_liters_100km(millas):
    km_100 = millas * 1609.344 / 1000 / 100
    litros = 3.785411784
    return litros / km_100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))