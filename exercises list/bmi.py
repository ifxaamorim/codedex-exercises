# Crie um programa que calcule seu próprio IMC.

altura = float(input("Digite o sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura ** 2)

print(imc)