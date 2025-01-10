## Crie um programa que fornece ao usuário previsões aleatórias da sorte.

import random

def sorte():
    frase = random.randint(1,8)

    if frase == 1:
        print("Não busque a felicidade - crie-a")
    elif frase == 2:
        print("Todas as coisas são difíceis antes de serem fáceis.")
    elif frase == 3:
        print("O pássaro madrugador pega a minhoca, mas o segundo rato pega o queijo.")
    elif frase == 4:
        print("Alguém em sua vida precisa de uma carta sua.")
    elif frase == 5:
        print("Não fique apenas pensando. Aja!")
    elif frase == 6:
        print("Seu coração vai pular uma batida.")
    elif frase == 7:
        print("A fortuna que você procura está em outro biscoito.")
    elif frase == 8:
        print("Ajude! Estou sendo mantido prisioneiro em uma padaria chinesa!")
    else:
        print("Error")

sorte()