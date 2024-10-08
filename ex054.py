from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range (1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        print('Já é maior de idade')
        totmaior = totmaior + 1
    else:
     print('Não é maior de idade')
     totmenor = totmenor + 1
print('Ao todo tivemos {} pessoas maiores e {} pessoas menores de idade.'.format(totmaior, totmenor))