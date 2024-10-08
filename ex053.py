frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1, -1, -1):  #tamanho da frase menos o ultimo espaço, indo até a primeira letra de traz pra frente
    inverso = inverso + junto
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase não é palindromo')