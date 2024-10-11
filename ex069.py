
tot18 = 0
totM = 0
totF = 0
while True:
    idade = int(input('Qual é a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo (M/F): ')).strip().upper()[0]
    if idade >= 18:
        tot18+= 1

    if sexo == 'M':
        totM += 1

    if sexo == 'F' and idade < 20:
        totF += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? (S/N)')).strip().upper()[0]
    if resp == 'N':
        break
print('ACABOU')
print(f'{tot18} tem mais de 18 anos')
print(f'{totM} homens foram cadastrados')
print(f'{totF} mulheres foram cadastradas')