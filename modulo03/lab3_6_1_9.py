''''
Descripción: Programa que elimina las repeticiones e imprime los valores unicos de la lista.
Autor: German Venado
Fecha: 06 Oct 2022
'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

list_act = my_list
list_act [0:9]
for val in my_list:
    if val in my_list:
        del my_list[val]

print("La lista con elementos únicos: ")
print(my_list)