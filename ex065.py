resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':    #enquanto resposta estiver em Sim
    num = int(input('Digite um numero: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num

    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} numeros, e a média é {}'.format(quant, media))
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))
print('ACABOU')