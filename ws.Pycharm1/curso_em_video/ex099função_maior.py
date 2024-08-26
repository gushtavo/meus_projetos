from time import sleep


def maior(* valor):
    cont = maior = 0
    print('=-' * 30)
    print('Analisando os Valores passados...')
    for num in valor:
        print(num, end=' ')
        sleep(0.3)
        if cont == 0:
            maior = num
        elif num > maior:
            maior = num
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    #print(f'Foram informados {len(valor)} valores ao todo.')
    #print(f'O maior valor informado foi {max(valor)}')


maior(4, 2, 7, 1, 5)
maior(7, 9, 10, 5)
maior(15, 78, 93, 50, 34)
maior()
