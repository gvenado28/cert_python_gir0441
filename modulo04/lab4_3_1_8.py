''''
Descripción: Función que tomará tres elementos como aaa/mm/dd y devolverá el día correspondiente del año(n/366).
Autor: German Venado
Fecha: 21 oct 2022
'''

def is_year_leap(year): # Definir la función de año bisiesto en formato de año
    # Condicional del año bisiesto.
    if year % 4 == 0: # Si el sobrante de la div del año entre 4 es 0 es bisiesto.
        return True
    elif year % 100 == 0: # Si el sobrante de la div del año entre 100 es 0 no es bisiesto.
         return False
    elif year % 400 == 0: # Si el sobrante de la div del año entre 400 es 0 es bisiesto.
        return True

def days_in_month(year, month): # Definir la función de los días que tiene un mes.
	if year < 1582 or month < 1 or month > 12: # Condición si se sobrepasa el número de días y meses.
		return None 
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Arreglo con límites de días de cada mes.
	day_month  = days[month - 1]
	if month == 2 and is_year_leap(year): #Condición para el mes de febrero si es año bisiesto.
		day_month = 29
	return day_month

def day_of_year(year, month, day): # Definir la función de la fecha completa.
	days = 0
	for d in range(1, month): 
		md = days_in_month(year, d)
		if md == None:
			return None
		days += md
	md = days_in_month(year, month)
	if day >= 1 and day <= md:
		return days + day
	else:
		return None

print(day_of_year(2000, 12, 31))