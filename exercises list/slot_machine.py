import random

simbolo = ["🍒", "🍇", "🍉", "7️⃣"]

resultado = random.choices(simbolo, k=3)

print(f"{resultado[0]} | {resultado[1]} | {resultado[2]}")

if resultado == ["7️⃣", "7️⃣", "7️⃣"]:
    print("Parabéns. Recebeu o prêmio! 💰")
else:
    print("Não foi desta vez. Obrigado por jogar!")