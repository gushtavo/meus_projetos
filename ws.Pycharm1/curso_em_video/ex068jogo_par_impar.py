from random import randint
print('=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 30)
cont = 0
while True:
    soma = 0
    computador = randint(0, 10)
    voce = int(input('Digite um valor: '))
    par_impar = ' '
    while par_impar not in 'PI':
        par_impar = input('Par ou Ímpar (P/I): ').strip().upper()[0]
    print('-' * 40)
    soma = computador + voce
    print(f'Você jogou {voce} e o computador {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 40)
    if soma % 2 == 0:
        if par_impar in 'P':
            cont += 1
            print('você VENCEU!')
        elif par_impar in 'I':
            print('Você PERDEU !')
            break
    elif soma % 2 != 0:
        if par_impar in 'I':
            cont += 1
            print('Você VENCEU!')
        elif par_impar in 'P':
            print('Você PERDEU!')
            break
    print('Vamos jogar Novamente...')
    print('=' * 40)
print('=' * 40)
print(f'GAME OVER! Você Venceu {cont} vezes')
