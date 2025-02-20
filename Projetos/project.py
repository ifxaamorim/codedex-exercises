## Projeto do curso final de python. Um jogo de adivinhação de palavras estilo forca.

import random

print ("Bem-vindo ao jogo de adivinhe a palavra 🧩 \nSua missão é adivinhar a palavra correta com apenas 10 tentativas. \nSerá que você consegue? Vamos lá ")
banco_de_palavras = ["mesa", "blusa", "faculdade", "fruta", "codedex", "vscode"]

palavra = (random.choice(banco_de_palavras))

adv_palavras = ['_'] * len(palavra)

tentativas = 10
erros = 0

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
        erros += 1
        print("Palpite errado! Suas tentativas restantes: " + str(tentativas))
        if erros == 4:
            dica = random.choice([letra for letra in palavra if letra not in adv_palavras])
            print(f"Dica: A palavra contém a letra '{dica}'")
    if "_" not in adv_palavras:
        print("\nParabéns!! Você acertou a palavra: " + palavra)
        break
else:
    print("\nVocês ficaram sem tentativas! A palavra era: " + palavra)