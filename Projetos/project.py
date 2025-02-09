## Projeto do curso final de python 

import random


banco_de_palavras = ["mesa", "blusa", "faculdade", "fruta"]

palavra = (random.choice(banco_de_palavras))

adv_palavras = ['_'] * len(palavra)

tentativas = 10

while tentativas > 0:
    print('\nPalavra atual: ' + ' '.join(adv_palavras))
    adivinhe = input("Adivinhe uma letra: ")
    if adivinhe in palavra:
        for i in range(len(palavra)):
            if palavra[i] == adivinhe:
                adv_palavras[i] = adivinhe
        print("Ótimo palpite!")
    else:
        tentativas -= 1
        print("Palpite errado! Suas tentativas restantes: " + str(tentativas))
    if "_" not in adv_palavras:
        print("\nParabéns!! Você acertou a palavra: " + palavra)
        break
else:
    print("\nVocês ficaram sem tentativas! A palavra era: " + palavra)