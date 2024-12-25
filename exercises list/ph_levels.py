# Crie um programa que verifica se um nível de pH é básico, ácido ou neutro.

ph = int(input("Insira o valor do PH entre 0 e 14: "))

if ph > 7:
    print("Básico")
elif ph < 7:
    print("Ácido")
else:
    print("Neutro")