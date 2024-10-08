n1, n2 = map(float, input('Digite 2 valores qualquer: ').split())
print(''' O que deseja realizar? 
[ 0 ] soma
[ 1 ] subtração
[ 2 ] multiplicação
[ 3 ] divisão''')
botao = int(input('Escolha entre 0 e 3: '))
if botao == 0:
    soma = n1 + n2
    print('A soma é {}'.format(soma))
elif botao == 1:
    sub = n1 - n2
    print('A subtração vale {}'.format(sub))
elif botao == 2:
    mult = n1 * n2
    print('A multiplicação é {}'.format(mult))
elif botao == 3:
    div = n1 / n2
    print('A divisão é {}'.format(div))
else:
    print('tente novamente')
