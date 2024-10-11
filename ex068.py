from random import randint
v = 0
while True:

    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer jogar par ou impar? [P/I] ')).strip().upper()[0]

    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU!')
            v = v + 1
        else:
            print('VOCÊ PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v = v + 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos jogar novamente...')
print('GAME OVER')
print(f'você venceu {v}')