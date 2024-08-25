'''
# Filter função
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, por item. (list, tuple, dict, etc.)
'''

valores = [10, 12, 29, 37, 56]


def remover_20(x):
    return x > 20


acima_20 = filter(remover_20, valores)
print(list(acima_20))

print(list(filter(remover_20, valores)))
