somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
for p in range (1, 5):
     print('============{}a Pessoa============='.format(p))
     nome = input('Digite seu nome: ').strip()
     idade = input('Digite sua idade: ')
     sexo = input('Digite seu sexo: ').strip()
     somaidade = somaidade + 1
     if p == 1 and sexo in 'Mm':
         maioridadehomem = idade
         nomevelho = nome


mediaidade = somaidade / 4
print('A média de idade dessas 4 pessoas é: {}'.format(mediaidade))