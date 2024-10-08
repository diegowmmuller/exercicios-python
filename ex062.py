print('Calculo de Progressão Aritmética')
pt = int(input('Digite um numero: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont < total:
        print('{} > '.format(termo), end='')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')