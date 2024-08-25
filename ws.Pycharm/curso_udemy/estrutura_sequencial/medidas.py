quadrado: float; triangulo: float; trapezio: float

a = float(input('Digite a medida A: '))
b = float(input('Digite a medidda B: '))
c = float(input('Digite a medida C: '))

quadrado = a * a
triangulo = (a * b) / 2
trapezio = ((a + b) * c) / 2
print()
print(f'AREA DO QUADRADO = {quadrado:.4f}')
print('AREA DO TRINAGULO = {:.4f}'.format(triangulo))
print(f'AREA DO TRAPEZIO = {trapezio:.4f}')
