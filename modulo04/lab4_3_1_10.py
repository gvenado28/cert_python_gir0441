''''
Descripción: Programa que hará conversiones (km/mill, l/gal).
Autor: German Venado
Fecha: 21 oct 2022
'''
#definir la variable para el dato de los litros
def liters_100km_to_miles_gallon(liters):
    milla = (100*1000) / 1609.344 # Conversión de milla, dividiendo los 100km entre los metros que equivalen a una milla.
    galon = liters / 3.785411784 # Conversión de galon, dividiendo los litros entre los litros que equivalen a un galon.
    return milla / galon # Obtener el valor de milla por galon (mpg).
    
def miles_gallon_to_liters_100km(millas):
    gal_lit = 3.785411784 # Cantidad de litros en galones.
    km_100 = millas * 1609.344 / 100 / 1000 # Conversión de millas a 100km.
    return gal_lit / km_100 # Valor viceverso de litros sobre 100km (l/100km).

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))