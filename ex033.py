num1 = int(input('digite um numero qualquer'))
num2 = int(input('digite outro numero qualquer'))
num3 = int(input('Digite mais um numero qualquer'))
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
print('O menor numero digitado é {}'.format(menor))
