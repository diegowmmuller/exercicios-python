tot = 0
totmil = 0
menor = 0
cont = 0
while True:
    nameproduct = str(input('nome do produto: '))
    preco = float(input('Qual é o preço do produto?R$ '))
    cont = cont + 1
    tot = tot + preco
    if preco >= 1000:
        totmil = totmil + 1

    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? (S/N)')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total é: {tot}')
print(f'temos {totmil} produtos custando mais de 1000R$')
print(f'O produto mais barato custa {menor}R$')