def jogador(nome='', gol=0):
    if nome.strip() == '':
        nome = '<Desconhecido>'
    return f'O jogador {nome.strip()} fez {gol} gol(s) no Campeonato.'


print('~' * 30)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
print(jogador(n, g))
