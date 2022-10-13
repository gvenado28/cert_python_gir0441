''''
Descripción: Utilizar la sentencia if-elif-else.
Autor: German Venado
Fecha: 20 sep 2022
'''

year = int(input("Introduce un año: "))

if(year <= 1580): 
    print('No esta dentro del período del calendario Gregoriano')
elif year % 4 !=0:
    print('Año común')
elif year % 100 !=0:
    print('Año bisiesto')
elif year % 400 !=0:
    print('Año común')
else:
    ('Año bisiesto')