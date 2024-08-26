'''
# Lambda - Function
    # É uma função (pequena) sem nome
    # pode ter varios argumentos mais somente 1 expressão
    # muito utilizada dentro de outras funções
    # Codigo mais clean.
'''
# somar10 = lambda x, y: x + y + 10


# print(somar10(4, 7))

# lambda dentro da função

def somar(x):
    def func2(x): return x + 10
    return func2(x) * 4


print(somar(2))
