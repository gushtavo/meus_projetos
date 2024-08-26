def leiaint(num):
    while True:
        valor = input(num)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


n = leiaint('Digite um Número: ')
print(f'Você acabou de Digitar o Número {n}.')


#versão_curso_em_video
'''def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor'''
