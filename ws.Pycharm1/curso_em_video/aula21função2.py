def contador(i, f, p):
    """
    ->faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem return
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('fim!')


#help(contador)


#parâmetros opcionais
def somar(a=0, b=0, c=0):
    """
    -> faz a soma de tres valores e mostra na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem return
    função criada por Gustavo
    """
    s = a + b + c
    print(f'A soma vale {s}')


#help(somar)
#somar(3, 2, 5)
#somar(5, 7)

#escopos variaveis
def teste(n):
    global n1
    n += 4
    n1 = 4
    print(f'N dentro vale {n}')
    print(f'N1 dentro vale {n1}')


n1 = 2
#teste(n1)
#print(f'N1 fora vale {n1}')


#retornando valores #-> return
def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
#print(f'Meus cálculos foram {r1}, {r2}, {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#n = int(input('Digite um numero: '))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(7)
f2 = fatorial(4)
f3 = fatorial()
#print(f'Os resultados são {f1}, {f2}, {f3}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
