jogador = dict()
gol = []
jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas Partidas {jogador['nome'].upper()} jogou? '))
for p in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {p + 1}: ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
#soma = 0
#for s in gol:
    #soma += s
#jogador['total'] = soma #minha_versão
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k.upper()} tem valor {v}.')
print('-=' * 30)
print(f'O Jogador {jogador['nome']} Jogou {len(jogador['gols'])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => Na partida {i + 1}, fez {v} gols.')
#for p in range(0, partidas):
    #print(f'    => Na partida {p + 1}, fez {jogador['gols'][p]} gols.') #minha_versão
print(f'Foi um total de {jogador['total']} Gols.')
