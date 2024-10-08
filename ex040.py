n1 = float(input('Digite aqui a sua primeira nota: '))
n2 = float(input('Digite agora sua segunda nota: '))
media = (n1 + n2)/2
if media < 5.0:
    print('Você está reprovado, sua média é {}'.format(media))
elif media == 5.0 or media <= 6.9:
    print('Você está de recuperação, sua média é {}'.format(media))
else:
    print('Você está aprovado, parabéns! Sua média é {}'.format(media))