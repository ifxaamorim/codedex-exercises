## Projeto de um mini game usando o terminal com conceitos visto no módulo 1 ao 4.
## Em inglês pois o código precisa passar pela avalição dos mentores da plataforma

jogador = 0

print(" -- Game terminal: Late for school --")

print("Today is Tuesday and you need to get to college early to present your new project, but you woke up late because you went to bed late the day before.")

print("You live 15 km from the college and need to get there as quickly as possible. Based on your choices, you need to arrive by 8:00 am. Lets go? ")

print("-------------------------")

print("(QS1) Are you going by car, metro or bus? ? ")

print(" 1) Car")
print(" 2) Metro")
print(" 3) Bus")

resposta = int(input("(1-3):"))

if resposta == 1:
    jogador += -2
elif resposta == 2:
    jogador += 1
elif resposta == 3:
    jogador += 1
else:
    print("Invalid data")

print("(QS2:) Will you take the shortest or the longest route? ")

print("1) Short")
print(" 2) Long")

resposta = int(input("(1-2):"))

if resposta == 1:
    jogador += 2
elif resposta == 2:
    jogador += 1
else:
    print("Invalid data")

print("(QS3:) Are you going to stop by the coffeshop or not? ")

print(" 1) Yes")
print(" 2) No")

resposta = int(input("(1-2):"))

if resposta == 1:
    jogador += -1
elif resposta == 2:
    jogador += 1

print("-------------------------")

if jogador < 0:
    print("You were late for college 🚫")
else:  
    print("You got to college on time  🏁")

print("-------------------------")

print("End of game")