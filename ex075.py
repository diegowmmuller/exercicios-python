num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores  {num}.')
print(f'O numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado.')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')