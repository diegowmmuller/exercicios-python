from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    print('Você ainda não tem 18 anos.')
else:
    print('Você já passou do período de alistamento militar')