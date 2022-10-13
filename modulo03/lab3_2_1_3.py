''''
Descripción: Hacer un juego de número secreto, donde se adivine el número secreto se termine el juego.
Autor: German Venado
Fecha: 20 sep 2022
'''

secret_number = 777

print(
"""
    +==================================+
    | ¡Bienvenido a mi juego, muggle!  |
    | Introduce un número entero       |
    | y adivina que número he          |
    | elegido para ti.                 |
    | Entonces,                        |
    | ¡Cuál es el número sercreto?     |
    +==================================+
""")

number = int(input("Ingresa tú número "))

if(secret_number == number): 
    print("¡Bien hecho, muggle! Eres libre ahora!")
else:
    while secret_number != number:
        print('Ja, ja, ¡Estás atrapado en mi bucle!')
        int(input('¿Cuál es el número secreto? '))
        break
    print(
        """
        +==================================+
        | ¡Bienvenido a mi juego, muggle!  |
        | Introduce un número entero       |
        | y adivina que número he          |
        | elegido para ti.                 |
        | Entonces,                        |
        | ¡Cuál es el número sercreto?     |
        +==================================+
        """)