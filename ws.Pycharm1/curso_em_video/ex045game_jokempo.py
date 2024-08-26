from random import randint
from time import sleep
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
lista = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
jogador = int(input('Qual é a sua jogada: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)
print(f'Computador jogou {lista[computador]}')
print(f'Jogador jogou {lista[jogador]}')
print('-=' * 10)
if lista[jogador] == lista[computador]:
    print('EMPATE')
elif computador == 0:
    if jogador == 1:
        print('Jogador VENCEU')
    elif jogador == 2:
        print('Computador VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('Computador VENCEU')
    elif jogador == 2:
        print('Jogador VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('Jogador VENCEU')
    elif jogador == 1:
        print('Computador VENCEU')
    else:
        print('JOGADA INVÁLIDA')
