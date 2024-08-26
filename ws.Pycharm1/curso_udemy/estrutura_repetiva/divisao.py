c = int(input('quantos casos voce vai digitar: '))

divisao: float
for i in range(c):
    n = float(input('entre com numerador: '))
    d = float(input('entre com denominador: '))

    if d == 0:
        print('DIVISAO IMPOSSIVEL')
    else:
        divisao = n / d
        print(f'DIVISAO = {divisao:.1f}')
