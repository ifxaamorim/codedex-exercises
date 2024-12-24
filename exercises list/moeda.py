#Crie um programa que pergunte ao usuário o valor que ele tem em pesos, soles e reais e calcule o total em USD.

pesosC = int(input("Qual valor você tem em Pesos colombianos? "))

solasP = int(input("Qual valor você tem em Solas peruanas? "))

realB = int(input("Qual valor você tem em Reais brasileiros? "))

total_sobras = pesosC * 0.001405 + solasP * 1.000  + realB * 0.25 

print(total_sobras)