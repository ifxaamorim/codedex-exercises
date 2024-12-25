ph = int(input("Insira o valor do PH entre 0 e 14: "))

if ph > 7:
    print("Básico")
elif ph < 7:
    print("Ácido")
else:
    print("Neutro")