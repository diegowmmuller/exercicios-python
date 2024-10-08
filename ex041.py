from datetime import date
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('O atléta nasceu em {} e possui {} anos.'.format(ano, idade))
if atual - ano <= 9:
    print('Atléta mirim')
elif atual - ano <= 14:
    print('Atléta infantil')
elif atual - ano <= 19:
    print('Atleta junior')
elif atual - ano <= 20:
    print('Atléta senior')
else:
    print('Atléta master')