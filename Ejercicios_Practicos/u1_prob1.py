''''
Descripción: 
Autor: German Venado
Fecha: 13 oct 2022
'''
import math

a = int(input("¿Cuánto vale a? "))
b = int(input("¿Cuánto vale b? "))
c = int(input("¿Cuánto vale c? "))

def raiz(a, b, c):
    x1 = (b + math.sqrt( ((b*b) - (4*a*c)))) / (2 * a)
    x2 =  (b - math.sqrt( ((b*b) - (4*a*c)))) / (2 * a)
    print("x1= ", x1)
    print("x2= ", x2)
print(raiz(a, b, c))