"""catop = float(input('Comprimento do Cateto Oposto: '))
catad = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = (catop ** 2 + catad **2) **0,5 #elevado a meio é igual a raiz quadrada
print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))"""
import math
catop = float(input('Comprimento do cateto oposto: '))
catad = float(input('Comprimentoo do cateto adjacente: '))
hi = math.hypot(catad,catop)
print('A Hipotenusa vai medir {:.2f}'.format(hi))