a = open("devices.txt", "r")
opc = 'exit'

while True:
    newItem = input('')
    a.write(newItem + “\n”)
    if opc == 'exit':
        break
    print('¡Todo listo!')