''''
Descripción: Función qeu toma dos argumentos como año y mes para saber el número de días de dicho mes/año.
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

test_years = [1900, 2000, 2016, 1987] # Arreglo de datos con años.
test_months = [ 2, 2, 1, 11] # Arreglo de datos de meses.
test_results = [28, 29, 31, 30] # Arreglo de datos de días.
for i in range(len(test_years)): # Bucle for
	yr = test_years[i]
	mo = test_months[i]
	print(yr,mo,"-> ",end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")