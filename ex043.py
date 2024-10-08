peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Abaixo do peso, imc = {:.2f}'.format(imc))
elif 18.5 >= imc < 25:
    print('Peso ideal, imc = {:.2f}'.format(imc))
elif imc == 25 <= 30:
    print('Acima do peso, necessita cuidado, imc = {:.2f)'.format(imc))
elif imc == 30.01 <= 40:
    print('Obesidade, procure ajuda, seu imc é = {:.2f)'.format(imc))
else:
    print('Obesidade morbida, você morreu kkkkkk')