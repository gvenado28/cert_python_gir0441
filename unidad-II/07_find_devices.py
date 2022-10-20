file = open("devices.txt", "r")

for line  in file:
    line = line.strip()

    opc = input('¿Qué dispositivo desea buascar? ')
    if opc in line:
        print(line)
    else: print("Dcevices not font")

file.close()