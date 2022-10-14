''''
Descripción: 
Autor: German Venado
Fecha: 13 oct 2022
'''

n = int(input("Ingresa un valor mayor a cero: "))
num = 0

for num in reversed(range(n)):
    num += 2
    print(num - 1, end=", ")