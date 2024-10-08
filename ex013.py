print('============== Reajuste Salarial =============')
salario = float(input('Digite o valor do seu salário: '))
reajuste = salario*0.15
novosalario = salario + reajuste
print('O seu salario atual é {:.2f} e ele com o reajuste fica {:.2f}'.format(salario, novosalario))