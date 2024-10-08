print(f'{" LOJAS DIEGO ":=^40}')
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA CARTAO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de {:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    totparc = int(input('Quantas parcelas será o pgto? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {} de {:.2f}'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA')

print('Sua compra de {:.2f} R$ vai custar {:.2f} R$ no final '.format(preco, total))
