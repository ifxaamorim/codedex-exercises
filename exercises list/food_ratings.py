## D1 - Criar um sistema de classificação usando uma instrução if/ elif/ else:

nota = float (input("Insira sua avaliação (0 - 5): "))

if nota > 4.5:
    print("Extradordinário")
elif nota > 4:
    print("Excelente")
elif nota > 3:
    print("Bom")
elif nota > 2:
    print("Razoável")
else:
    print("Ruim")