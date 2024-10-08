num1 = int(input('Digite um numero qualquer: '))
num2 = int(input('Digite mais um numero qualquer: '))
if num1 > num2:
    print('O numero {} é maior que o {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior que o {}'.format(num2, num1))
else:
    print('Os numeros são iguais')