r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os SEGMENTOS acima podem formar um triangulo', end='')
    if r1 == r2 == r3:
        print('Triangulo EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('Triangulo ESCALENO!')
    else:
        print('Triangulo ISOCELES ')
else:
    print('Os SEGMENTOS acima não formam um triangulo')