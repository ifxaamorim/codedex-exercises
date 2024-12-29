# Crie um programa fizz_buzz.py que produza números de 1 a 100.
# Para múltiplos de 3, imprima "Fizz" em vez do número.
# Para múltiplos de 5, imprima "Buzz" em vez do número.
# Para múltiplos de 3 e 5, imprima "FizzBuzz".

for numero in range(1,101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
        