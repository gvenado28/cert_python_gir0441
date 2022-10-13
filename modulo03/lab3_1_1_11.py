''''
Descripción: Utilizaremos la sentencia if-else para ramificar una ruta de control.
Autor: German Venado
Fecha: 20 sep 2022
'''

income = float(input("Introduce el ingreso anual "))
tax = 0

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + 0.32 * (income-85528)

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("El impuesto es: ", tax, " pesos")