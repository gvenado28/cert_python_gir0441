''''
Descripción: Programa que lee números naturales y ejecuta los pasos de la hipótesis deLothar Collatz.
Autor: German Venado
Fecha: 29 sep 2022
'''

c0 = int(input("Ingresa un numero: "))
num = 0
if c0 < 1: 
    print("El  numero no debe ser 0 o negativo")
while c0 != 1: 
    if c0 % 2 == 0: 
      c0 = c0 / 2
    else: 
     c0= 3 * c0 + 1
    print(c0)
    num = num + 1 
print("Numero de pasos: ", num)