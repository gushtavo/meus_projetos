def lin(): #função sem Parâmetros
    print('-' * 30)


lin()
print('   JOGO DO CORINTHIANS   ')
lin()


def mensagem(msg): #função com parâmetros
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem(' Corinthians o maior do mundo ')
mensagem('       GUSTAVO GATO     ')


def soma(a, b):
    s = a + b
    print(f'A = {a} B = {b}')
    print(f'A soma de A + B vale {s}')


soma(5, 4)
soma(b=2, a=15)


def contador(* num):
    #for valor in num:
        #print(f'{valor} ', end='')
    #print()
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 3, 6, 9)
contador(8, 4, 1)
contador(7, 15)


def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [5, 8, 4, 13]
dobrar(valores)
print(valores)


def somas(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


somas(4, 7, 3)
somas(3, 9, 5, 8)
