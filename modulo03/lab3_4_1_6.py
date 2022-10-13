''''
Descripción: Remplazar un número de la lista e indicar el número de longitud de la lista después de borrar un elemento de la lista.
Autor: German Venado
Fecha: 29 sep 2022
'''

hast_list = [1, 2, 3, 4, 5] #Esta es una lista existente de número ocultos
hast_list[2] = input('Ingresa número: ')
del hast_list[4]
print(len(hast_list))
print(hast_list)