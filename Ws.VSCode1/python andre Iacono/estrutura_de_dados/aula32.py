'''
# generator expression
    # Uma forma mais rapida para lista, dicionarios e etc.
    # menos memoria alocada
    # valores em bytes
'''

from sys import getsizeof

valores = [i * 10 for i in range(10000)]
print(type(valores))
print(getsizeof(valores))

print('=' * 30)

valores = (i * 10 for i in range(10000))
print(type(valores))
print(getsizeof(valores))
