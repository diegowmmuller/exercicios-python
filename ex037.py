num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binario
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINARIO é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('O numero que você digitou é invalido, tente novamente!')