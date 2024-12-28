adivinha = 0
tentativa = 0

while adivinha != 6 and tentativa < 5:
  adivinha = int(input('adivinhe o número:  '))
  tentativa = tentativa + 1

if adivinha != 6:
  print('Você ficou sem tentativa.')
else:
  print('Você conseguiu!')