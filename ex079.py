numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado')
    else:
        print('Valor duplicado! Não Posso adicionar este valor')

    r = str(input('Quer continuar? [S/N]').upper())
    if r == 'N':
        break
print('=-'*45)
numeros.sort()
print(f'Você digitou os valores {numeros}')