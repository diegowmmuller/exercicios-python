times = ('corinthians', 'palmeiras', 'santos', 'gremio',
         'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
         'atletico', 'botafogo', 'atletico-pr', 'bahia',
         'sao paulo', 'fluminense', 'sport-recife',
         'ec vitoria', 'coritiba', 'avai', 'ponte preta',
         'atletico-go')
print('=-'*40)
print(f'lista de times {times}')
print('-='*40)
print(f'os 5 primeiros times são: {times[0:5]}')
print('-='*40)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-='*40)
print(f'a ordem alfabetica é: {sorted(times)}')
print('-='*40)
print(f'A chapecoense está na posição {times.index("chapecoense")+1}')
print('-='*40)