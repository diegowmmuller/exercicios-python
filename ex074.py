from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10),)
print('Os valores sorteados foram: ')
for n in num:
    print(f'{n} ', end='')


print(f'\no maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
