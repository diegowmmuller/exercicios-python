#n = float(input('Digite um numero: '))
#print('O numero digitado é {}'.format(n))
#print('O seu dobro é `{}'.format(n*2))
#print('O seu triplo é {}'.format(n*3))
#print('A sua raiz quadrada é {:.2f}'.format(n**0.5))

n = float(input('Digite um numero: '))
d = n*2
t = n*3
r = n**(1/2)  #também poderia ser n**0.5 (numero elevado a "meio")
print('O numero digitado é {}, seu dobro é {}, seu triplo é {} e sua raiz é {}'.format(n, d, t, r))