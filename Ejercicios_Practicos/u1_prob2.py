''''
Descripción: 
Autor: German Venado
Fecha: 13 oct 2022
'''

x = int(input("Ingresa el primer valor: "))
y = int(input("Ingresa el primer valor: "))

def nums_div(x, y):
    if x % y == 0:
        print(x, "es divisible entre ", y)
    else:
        print(x, "no es divisible entre ", y)
nums_div(x, y)