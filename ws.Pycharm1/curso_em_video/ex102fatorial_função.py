def fatorial(n, show=False):
    """
    -> Calcula O Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta
    :return: O valor Fatorial de um número n.
    """
    f = 1
    print('~' * 30)
    #minha_solução
    if show is True:
        for c in range(n, 0, -1):
            f *= c
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
        return f
    else:
        for c in range(n, 0, -1):
            f *= c
        return f


print(fatorial(4, False))
help(fatorial)
#solução_curso_em_video
'''for c in range(n, 0, -1):
    if show:
        print(c, end='')
        if c > 1:
            print(' X ', end='')
        else:
            print(' = ', end='')
    f *= c
return f'''