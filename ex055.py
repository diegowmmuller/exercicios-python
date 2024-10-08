maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('{}a Digite seu peso: '.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(maior)
print(menor)