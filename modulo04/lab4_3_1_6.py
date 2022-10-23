''''
Descripción: Función para verificar si un año es bisiesto o no.
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
    
test_data = [1900, 2000, 2016, 1987] # Arreglo que guarda los años.
test_result = [False, True, True, False] # Resultado esperado de los años bisiestos del arreglo anterior.

for i in range(len(test_data)): # Uso del bucle for imprimir un mensaje de acuerdo a su valor.
    yr= test_data[i]
    print (yr, "->", end="")
    result= is_year_leap(yr)
    if result == test_result[i]: # Condición: comparar si la operación de los años es igual al resultado esperado.
        print("OK")
    else:
        print("Fallido")