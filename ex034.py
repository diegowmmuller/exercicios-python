salario = float(input('Qual o salário do funcionario? '))
if salario <= 1250:
    novo =  salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.15)
print('Quem ganhava {:.2f} passa a ganhar {:.2f} agora.'.format(salario, novo))