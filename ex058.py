import random

print('Tente adivinhar em que numero estou pensando')
print('='*10)
acertou = False
while not acertou:
    numran = random.randint(0, 10)
    jogador = int(input('Qual é seu palpite? '))
    print(numran)
    if jogador == numran:
        acertou = True
print('Acertou')