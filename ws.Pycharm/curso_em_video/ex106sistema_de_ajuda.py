from time import sleep
c = ['\033[m',            #0 sem cores
     '\033[0;30;41m',     #1 vermelho
     '\033[0;30;42m',     #2 verde
     '\033[0;30;44m',     #3 azul
     '\033[0;30;43m']     #4 amarelo


def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO "{com}"', 3)
    sleep(1)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca -> '))
    if comando.strip().upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
