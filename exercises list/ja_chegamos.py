# Desafio: 1 - Já chegamos?

# Pergunte ao usuário “Já chegamos?”. Em seguida pergunte ao usuário “Já chegamos?” repetidamente até que ele responda “Sim”.


answer = input("Já chegamos?: ")

while answer != "Sim":
    print("Ainda não")
    answer = input("Já chegamos?: ")
print("Finalmente chegamos")