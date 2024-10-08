print('====PROGRAMA EMPRESTIMO BANCARIO====')
#informando os dados necessários
house = float(input('Qual o valor da casa? '))
salary = float(input('Quanto você ganha? '))
years = int(input('Em quantos anos você pretende pagar? '))
#realizando o calculo
# para saber qual sera o valor da prestacao é quantidade de anos * 12 dividido pelo valor da casa

prestacao = (years * 12) / house  #quantidade de meses é quantidade de anos * 12 que é a quantidade de meses

minimo = salary * 0.30 # Aqui calcula quanto é 30% do salario

print('Para pagar uma casa de {:.2f}R$ em {} anos, a prestação será de R$ {:.2f}.'.format(house, years, prestacao))

if prestacao <= minimo: #aq
    print('Emprestimo concedido')
else:
    print('Emprestimo negado')