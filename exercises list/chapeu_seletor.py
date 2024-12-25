# Objetivo desta atividade é fazer um algoritmo sobre uso de operadores lógicos e if/else com "O Chapéu Seletor"

Grifinória = 0
Corvinal = 0
LufaLufa = 0
Sonserina = 0

print("===============")
print("Chapéu Seletor")
print("===============")

print('Q1) Você prefere amanhacer ou anoitecer')

print('  1) Amanhecer')
print('  2) Anoitecer')

resposta = int(input("(1-2): "))

if resposta == 1:
    Grifinória += 1
    Corvinal += 1
elif resposta == 2:
    LufaLufa += 1
    Sonserina += 1
else:
    print("Dado invalido")

print("\nQ2) Quando eu morrer, quero que as pessoas se lembrem de mim como:")

print('  1) O bom')
print('  2) O grande')
print('  3) O sábio')
print('  4) O ousado')

resposta_2 = int(input("Escolha sua resposta (1-4): "))

if resposta_2 == 1:
    LufaLufa += 2
elif resposta_2 == 2:
    Sonserina += 2
elif resposta_2 == 3:
    Corvinal += 2
elif resposta_2 == 4:
    Grifinória += 2
else:
    print("Dado inválido")

print("nQ3)Que tipo de instrumento mais agrada seu ouvido?")

print(' 1) O violino')
print(' 2) O trompete')
print(' 3) O piano')
print(' 4) A bateria')

resposta_3 = int(input("Escolha sua resposta (1-4): "))

if resposta_3 == 1:
    Sonserina += 4
elif resposta_3 == 2:
    LufaLufa += 4
elif resposta_3 == 3:
    Corvinal += 4
elif resposta_3 == 4:
    Grifinória += 4
else:
    print("Entrada errada")

print("Grifinória:",Grifinória)
print("Corvinal:",Corvinal)
print("Lufa-Lufa:",LufaLufa)
print("Sonserina:",Sonserina)