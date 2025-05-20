#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_random = random.randrange (0,10)
num = int(input("Adivine un numero aleatorio entre el 0 y el 9: "))
while num != numero_random:
    num = int(input("Siga participando "))
print (f"El numero correcto es ", num)