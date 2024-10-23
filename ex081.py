lista = []
resposta = 'Nao'
while True:
    n = lista.append(int(input('Digite um valor a ser adicionado: ')))
    resposta = input('Quer continuar? [Sim/Nao]').strip().capitalize()

    if resposta == 'Nao':
        break

print('=-'*30)
print(lista)
print('=-'*30)
print(f'A lista contém {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A lista na ordem decrescente: {lista}')
if 5 in lista:
    print('O numero 5 está na lista.')
else:
    print('Não existe o numero 5 dentro da lista.')