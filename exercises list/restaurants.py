# Suponha que estamos criando um aplicativo de entrega de comida e queremos armazenar informações de restaurantes.

## Criação da classe 
class Restaurante:
    nome = ""
    categoria = ""
    nota = 0.0
    delivery = True


## Criação do objeto

bobs_burguer = Restaurante()

bobs_burguer.nome = "Bob\'s Burgers"
bobs_burguer.categoria = "American Diner"
bobs_burguer.nota = 4.7
bobs_burguer.delivery = False

print(vars(bobs_burguer))

therock = Restaurante()

therock.nome = "The Rokz Burger"
therock.categoria = "Australia Diner"
therock.nota = 4.0
therock.delivery = True

print(vars(therock))

acaibest = Restaurante()
acaibest.nome = "The best açaí"
acaibest.categoria = "Sorveteria"
acaibest.nota = 4.9
acaibest.delivery = False

print(vars(acaibest))

