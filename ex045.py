from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
#print('O computador escolheu {}'.format(itens[computador]))
print('-+='*10)
print('''SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-+=' * 11)
jogador = int(input('Qual é a sua jogada? '))
print('COMPUTADOR JOGOU {}'.format(itens[computador]))
print('JOGADOR JOGOU {}'.format(itens[jogador]))
print('-+=' * 11)
if computador == 0:
   if jogador == 0:
      print('EMPATE')
   elif jogador == 1:
      print('JOGADOR GANHOU')
   elif jogador == 2:
      print('COMPUTADR GANHOU')
   else:
      print('NUMERO INVALIDO, TENTE NOVAMENTE')
if computador == 1:
   if jogador == 0:
      print('COMPUTADOR GANHOU')
   elif jogador == 1:
      print('EMPATE')
   elif jogador == 2:
      print('JOGADOR GANHOU')
   else:
      print('NUMERO INVALIDO, TENTE NOVAMENTE')
if computador == 2:
   if jogador == 0:
      print('JOGADOR GANHOU')
   elif jogador == 1:
      print('COMPUTADOR GANHOU')
   elif jogador == 2:
      print('EMPATE')
   else:
      print('NUMERO INVALIDO, TENTE NOVAMENTE')
print('-+=' * 11)