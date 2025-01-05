## Desafio: 3 - Suponha que temos dois dados. 🎲 🎲

## Crie um jogo em que se adivinha o valor total depois de rolar um par de dados uma vez.

## Cada dado tem valores inteiros de 1 a 6. Como há dois dados, o intervalo de valores possíveis está entre 2 e 12 (inclusive).

import random

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)

total = dado1 + dado2

adivinhacao = 0

while adivinhacao != total:
    adivinhacao = int (input("Adivinhe a soma dos dois número:"))
    if adivinhacao != total:
        print("Errado. Tente novamente")
print("Parabéns. Você acertou")