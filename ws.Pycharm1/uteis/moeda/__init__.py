def metade(n=0, sit=False):
    n = n / 2
    if sit:
        return f'R${n:.2f}'
    else:
        return n


def dobro(n=0, sit=False):
    n *= 2
    """if sit:
        return f'R${n:.2f}'
    else:
        return n"""
    return n if not sit else moeda(n)


def aumentar(n=0, num=0, sit=False):
    valor = n + (n * num / 100)
    if sit:
        return f'R${valor:.2f}'
    else:
        return valor


def diminuir(n=0, num=0, sit=False):
    valor = n - (n * num / 100)
    """if sit:
        return f'R${valor:.2f}'
    else:
        return valor"""
    return valor if sit is False else moeda(valor)


def moeda(n=0):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n=0, aumento=0, reduzindo=0):
    print('~' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('~' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do Preço: \t{dobro(n, True)}')
    print(f'Metade do Preço: \t{metade(n, True)}')
    print(f'{aumento}% de Aumento: \t{aumentar(n, num=aumento, sit=True)}')
    print(f'{reduzindo}% de Redução: \t{diminuir(n, num=reduzindo, sit=True)}')
    print('~' * 30)
