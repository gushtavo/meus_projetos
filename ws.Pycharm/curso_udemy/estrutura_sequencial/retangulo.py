import math

area: float; perimetro: float; diagonal: float

base = float(input('base do retangulo: '))
altura = float(input('altura do retangulo: '))

area = base * altura
perimetro = 2 * base + 2 * altura
diagonal = math.sqrt(base ** 2 + altura ** 2)

print('AREA = {:.4f}'.format(area))
print(f'PERIMETRO = {perimetro:.4f}')
print(f'DIAGONAL = {diagonal:.4f}')
