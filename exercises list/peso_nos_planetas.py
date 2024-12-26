#Crie um programa de conversão de peso que
#Pergunta ao usuário qual é o seu peso na Terra.
#Solicita ao usuário um número de planeta.

print(" ====== ")
print(" Descubra seu peso atual no seu planeta favorito 🚀 ")
print(" ====== ")

peso_usuario = float (input("Digite seu peso atual: "))

print("Escolha seu planeta favorito (1-7)")

print(" 1 - Mercúrio")
print(" 2 - Vênus")
print(" 3 - Marte")
print(" 4 - Júpiter")
print(" 5 - Saturno	")
print(" 6 - Urano")
print(" 7 - Netuno")

planeta = int(input("(1-7): "))

if planeta == 1:
    print(peso_usuario * 0.38)
elif planeta == 2:
    print(peso_usuario * 0.91)
elif planeta == 3:
    print(peso_usuario * 0.38)
elif planeta == 4:
    print(peso_usuario * 2.53)
elif planeta == 5:
    print (peso_usuario * 1.07)
elif planeta == 6:
    print(peso_usuario * 0.89)
elif planeta == 7:
    print(peso_usuario * 1.14)
else:
    print("O número deste planeta não está disponível")


