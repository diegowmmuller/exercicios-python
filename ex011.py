print('====== PINTANDO PAREDE ==========')
largura = float(input('Qual é a largura da parede que irá pintar? '))
altura = float(input('Qual é a altura da parede?'))
area = altura*largura
tinta = area/2
print('A Área desta parede é {}m²'.format(area))
print('A quantidade de tinta necessária é {:.2f} Litros.'.format(tinta))
print('=================================')