# Crie um programa que possa responder a qualquer pergunta Sim ou Não com uma resposta diferente cada vez que for executado.
import random

pergunta = input("Qual sua pergunta: ")

numero_aleatorio = random.randint(1, 6)

if numero_aleatorio == 1:
    resposta = "Sim, definitivamente"
elif numero_aleatorio == 2:
    resposta = "É decididamente assim"
elif numero_aleatorio == 3:
    resposta = "Resposta nebulosa, tente novamente."
elif numero_aleatorio == 4:
    resposta = "Minhas fontes dizem que não."
elif numero_aleatorio == 5:
    resposta = "Pergunte novamente mais tarde."
elif numero_aleatorio == 6:
    resposta = "As perspectivas não são tão boas."
else:
    resposta = "Error"

print("Bola mágina: " + resposta)


