times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza',
         'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
         'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('=' * 30)
print('Lista de Times do Brasileirão: ', end='')
for pos, t in enumerate(times):
    print(f'{pos + 1}º:', t, end=' ')
print()
print('=' * 30)
print(f'Os 5 primeiros são: {times[:5]}')
print('=' * 30)
print(f'Os 4 Últimos são: {times[-4:]}')
print('=' * 30)
print(f'Times em ordem Alfabética: {sorted(times)}')
print('=' * 30)
print(f'O Corinthians está na {times.index('Corinthians') + 1}º Posição')
