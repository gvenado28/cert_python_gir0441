'''
Descripción: Mostrar las millas en kilometros y kilometros en millas.
Nombre: German Emiliano Venado Soria
Fecha: 22 Sep 2022
'''

kilometers = 12.25
miles = 7.38
miles_to_kilometros = miles * 1.61 / 1
kilometros_to_miles= kilometers * 1 / 1.61

print(miles, "Millas son" ,round(miles_to_kilometros, 2), "Kilometros")
print(kilometers, "Kilometros son" , round( kilometros_to_miles, 2), "Millas")