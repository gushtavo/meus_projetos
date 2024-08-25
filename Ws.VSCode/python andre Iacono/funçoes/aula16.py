# Varios argumentos com numeros => *agrs


def soma(*numeros):
    s = 0
    for num in numeros:
        s += num
    return s


total = soma(5, 7, 2)
print(total)

# Vários argumentos com strings e numeros => *agrs


def agencia(**carro):
    return carro


tabela = agencia(modelo='gol', cor='azul', motor=1.0)
print(tabela)
