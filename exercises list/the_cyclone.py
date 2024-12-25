# Atividade com operadores lógicos para criar umas regras para acesso de uma montanha-russa

altura = int(input("Insira sua altura:"))

credito = int(input("Insira valor do seu crédito: "))

if altura >= 137 and credito >= 10:
    print( "Aproveite o passeio" )
elif altura < 137 and credito >= 10:
    print( "Você não é alto o suficiente para andar" )
elif credito < 10 and altura >= 137:
    print( "Você não tem créditos suficientes" )
elif altura < 137 and credito < 10:
    print("Você não é alto o suficiente, nem tem créditos suficientes")
else:
    ("Error")
