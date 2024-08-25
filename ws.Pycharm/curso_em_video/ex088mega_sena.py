from time import sleep
from random import randint
print('=' * 30)
print(f'{"MEGA SENA":^30}')
print('=' * 30)
jogos = []
lista = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, quant):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('=-' * 3, f' SORTEANDO {quant} JOGOS ', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i + 1}: {l}')
    sleep(1)
print('=-' * 5, ' BOA SORTE! ', '=-' * 5)
