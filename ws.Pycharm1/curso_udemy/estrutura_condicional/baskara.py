import math

delta: float; x1: float; x2: float

a = float(input('COEFICIENTE A: '))
b = float(input('COEFICIENTE B: '))
c = float(input('COEFICIENTE C: '))

delta = (b * b) - (4 * a * c)

if delta < 0:
    print('Esta equação nao possui raizes reais')
else:
    x1 = ((-b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-b) - math.sqrt(delta)) / (2 * a)

    print('X1 = {:.4f}'.format(x1))
    print(f'X2 = {x2:.4f}')
