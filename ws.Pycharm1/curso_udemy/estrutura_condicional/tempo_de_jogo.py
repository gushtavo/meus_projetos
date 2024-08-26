jogo: int

inicial = int(input('Hora inicial: '))
final = int(input('Hora final: '))

if final > inicial:
    jogo = final - inicial
else:
    jogo = 24 - (inicial - final)

print(f'O JOGO DUROU {jogo} HORA(S)')
