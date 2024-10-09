
while True:
    print('=' * 45)
    num = int(input('Quer descobrir a tabuada de qual numero? '))
    print('=' * 45)
    if num < 0:
        break
    for i in range (1, 11):
        print(f'{i} x {num} = {i*num}')
    print('=' * 30)
print('PROGRAMA ENCERRADO')