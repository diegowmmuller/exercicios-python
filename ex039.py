anonasc = int(input('Em que ano você nasceu? '))
apto = 2024 - anonasc
if apto <= 17:
    print('Parabéns! Você esta chegando perto do periodo de alistamento')
elif apto == 18:
    print('É HORA DE SE ALISTAR NO EXERCITO!')
else:
    print('Você não está mais no período do alistamento militar.')