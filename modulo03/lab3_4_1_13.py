Beatles = []

print("Paso 1: ", Beatles)

Beatles.append('Jhon Lennon')
Beatles.append('Paul McCartney')
Beatles.append('George Harrison')
print("Paso 2: ", Beatles)

for i in range(2):
    Beatles.append(input('Agrega otro miembro: '))
print("Paso 3: ", Beatles)

del Beatles[3, 4]
print("Paso 4: ", Beatles)

Beatles.insert(0, 'Ringo Start')
print("Paso 5: ", Beatles)