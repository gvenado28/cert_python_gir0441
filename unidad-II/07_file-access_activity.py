a = open("devices.txt", "r")
opc = 'exit'

while True:
    newItem = input('¿Qué dispositivo ',+
    'desea agregar? ')
    a.write(newItem + '\n')
    if opc == 'exit':
        break
    print('¡Todo listo!')

'''
CORECCIÓN

file = open("devices.txt", "a")
newItem = ''

while True:
    newItem = input('¿Qué dispositivo desea agregar? ')

    if newItem == 'exit':
        print('¡Todo listo!')
        break
    
file.write(newItem + '\n')
file.close()'''