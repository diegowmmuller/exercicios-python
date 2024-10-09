soma = cont = 0
while True:
    num = int(input('Digite um valor '))

    if num == 999:
        break
    soma = soma + num
    cont = cont + 1
print(f'A soma dos numeros é {soma}')
print(f'O numero de tentativas é {cont}')