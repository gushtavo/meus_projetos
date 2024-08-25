from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for num in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somapar():
    soma = 0
    for p in numeros:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores Pares de {numeros}, Temos {soma}')


numeros = list()
sorteia()
somapar()
