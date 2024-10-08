print('Calculo de Progressão Aritmética')
pt = int(input('Digite um numero: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 1
while cont < 10:
    print('{} > '.format(termo), end='')
    termo = termo + r
    cont = cont + 1
print('FIM')