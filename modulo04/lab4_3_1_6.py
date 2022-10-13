''''
Descripción: Función para verificar si un año es bisiesto o no.
Autor: German Venado
Fecha: 06 oct 2022
'''

def is_year_leap(year):
    if year % 4 == 0 and ((year % 100 !=0) or (year & 400 == 0)):
        resp = True
    else:
        resp = False
        return(resp)
    
test_data = [1900, 2000, 2016, 1987]
test_result = [False, True, True, False]

for i in range(len(test_data)):
    yr= test_data[i]
    print (yr, "->", end="")
    result= is_year_leap(yr)
    if result == test_result[i]:
        print("OK")
    else:
        print("Fallido")