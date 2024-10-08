import random
num = int(input('Digite um numero qualquer entre 0 e 5: '))
numran = random.randint(0, 5)
if numran == num:
    print('Parabéns, você acertou!')
else:
    print('Que pena, eu pensei no numero {}'.format(numran))