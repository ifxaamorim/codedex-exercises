# Pergunte ao usuário o número do mês usando a input()função.
# Verifique as quatro estações usando uma instrução if/ elif/ elsee operadores lógicos.

mes = int(input("Insira seu mês favorito: "))

if mes == 1 or mes == 2 or mes == 3:
    print("Inverno 🌨️")
elif mes == 4 or mes == 5 or mes == 6:
    print("Primavera 🌱")
elif mes == 7 or mes == 8 or mes == 9:
    print("Verão 🌻")
elif mes == 10 or mes == 11 or mes == 12:
    print("Outono 🍂")
else:
    print("Inválido")