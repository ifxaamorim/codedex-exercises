
def get_itens(opcao):
    
    if opcao == 1:
        return "🍔 Cheeseburger"
    elif opcao  == 2:
        return "🍟 Fries"
    elif opcao == 3:
        return "🥤 Soda"
    elif opcao == 4:
        return "🍪 Cookie"
    elif opcao == 5:
        return "🍟 Fries"
    else:
        return "Ops! Inválido"
    
    
def welcome():
    print("Bem vindo ao nosso restaurante. O que você vai comer hoje")
    print("1 - 🍔 Cheeseburger")
    print("2 - 🍟 Fries")
    print("3 - 🥤 Soda")
    print("4 - 🍦 Ice Cream")
    print("5 - 🍪 Cookie")

welcome()

opcao = int(input("Insira o numero do pedido: "))
print(get_itens(opcao))
