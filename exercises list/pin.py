3# Exercicio sobre loop while introdutório

print(" ===== BANK OF CODÉDEX ===== ")

pin = int(input("Insira sua senha: "))

while pin != 1234:
  pin = int(input("Senha incorreta. Digite sua senha novamente: "))

if pin == 1234:
  print("Senha correta")