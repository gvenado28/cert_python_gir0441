''''
Descripción: 
Autor: German Venado
Fecha: 13 oct 2022
'''

Nombres=[]
print("Nombres:", Nombres)

Nombres.append ("Luis")
Nombres.append ("Pedro")
Nombres.append ("Paco")
Nombres.append ("Arturo")
print("Nombres:", Nombres)
del Nombres[3]
Nombres.insert(3, "Gustavo")
print("Nombres:", Nombres)

for miembros in Nombres:
    print(miembros)