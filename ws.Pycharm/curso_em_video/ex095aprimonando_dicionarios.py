dados = list()
jogador = dict()
gol = []
while True:
    jogador.clear()
    gol.clear()
    print('-' * 30)
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas Partidas {jogador['nome']} jogou: '))
    for p in range(0, partidas):
        gol.append(int(input(f'Quantos gols na Parida {p + 1}: ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    dados.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar (S/N): ')).strip().upper()
        if continuar[0] in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if continuar[0] in 'N':
        break
print('-=' * 30)
print(f'{"Cod":<4}{"NOME":<15}{"Gols":<15}{"Total":<15}') #minha_versão
#print('Cod ', end='')
#for i in jogador.keys():
    #print(f'{i:<15}', end='')
#print()
print('-' * 40)
for i, v in enumerate(dados):
    print(f'{i:>3} ', end='')
    for j in v.values():
        print(f'{str(j).upper():<15}', end='')
    print()
while True:
    print('-' * 40)
    mostrar = int(input('Mostar dados de qual Jogador: '))
    if mostrar == 999:
        break
    if mostrar <= len(dados) - 1:
        print(f'  --  LEVANTAMENTO DO JOGADOR {dados[mostrar]['nome'].upper()}')
        for i, v in enumerate(dados[mostrar]['gols']):
            print(f'      No Jogo {i + 1} fez {v} Gols.')
    else:
        print(f'ERRO! não existe jogador com código {mostrar}! Tente Novamente.')
print('<< Volte Sempre >>')
