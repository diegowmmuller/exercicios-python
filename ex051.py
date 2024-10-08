primeiro = int(input('Digite o primeiro numero: '))
razao = int(input('Digite a razao: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print('{}'.format(i))