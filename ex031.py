km = float(input('Quantos quilometros você irá percorrer?'))
if km <= 200:
    km1 = km * 0.50
    print('A distanca percorrida em km é {}  e o preço a pagar é {:.2f}'.format(km, km1))
else:
    km2 = km * 0.45
    print('A distancia percorrida em km é {} e o preço  a pagar é {:.2f}'.format(km, km2))