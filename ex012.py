print('======== calculando descontos ===========')
preco = float(input('Qual é o valor deste produto? '))
desconto = preco * 0.05  # 5% de desconto
newprice = preco - desconto
print("O preço original é {}".format(preco))
print('O valor do desconto é: {:.2f}'.format(desconto))
print('O valor final fica: {:.2f}'.format(newprice))