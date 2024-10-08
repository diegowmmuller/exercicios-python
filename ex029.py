velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('Multado! você excedeu o limite de velocidade de 80 km/h!')
    multa = (velocidade - 80) * 7
    print('O valor da multa é {:.2f} R$.'.format(multa))
else:
    print('Dentro do limite de velocidade, boa viagem!')