# D3 - Use o random módulo para criar um número de 0 a 5.
# Em seguida, use uma instrução if/ elif/ elsepara imprimir um desses seis fatos aleatórios do Snapple

import random

numero = random.randint(0, 5)

if numero == 0:
    print("Flamingos turn pink from eating shrimp.")
elif numero == 1:
    print("The only food that doesn\'t spoil is honey.")
elif numero == 2:
    print("Shrimp can only swim backwards.")
elif numero == 3:
    print("A taste bud\'s life span is about 10 days.")
elif numero == 4:
    print("It is impossible to sneeze while sleeping.")
elif numero == 5:
    print("It is illegal to sing off-key in North Carolina.")
else:
    print("Error")

