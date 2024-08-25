from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for num in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for p in lista:
        if p % 2 == 0:
            soma += p
    print(f'Somando os valores Pares de {lista}, Temos {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)
