secret_number = 777
number = int(input("Ingresa tú número "))

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

number = int(input())

while secret_number != number:
    print('Ja, ja, ¡Estás atrapado en mi bucle!')
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