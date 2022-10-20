a = open("devices.txt", "r")
opc = 'exit'

while True:
    newItem = input('¿Qué dispositivo ',+
    'desea agregar?')
    a.write(newItem + “\n”)
    if opc == 'exit':
        break
    print('¡Todo listo!')

