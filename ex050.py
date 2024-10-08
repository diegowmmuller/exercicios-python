soma = 0
cont = 0
for i in range (1, 7):
    num = int(input('Digite o {}o numero: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} numeros é a soma foi {}'.format(cont, soma))