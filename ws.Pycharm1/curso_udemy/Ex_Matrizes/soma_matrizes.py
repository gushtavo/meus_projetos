m = int(input('Quantas linhas vai ter cada matriz? '))
n = int(input('Quantas colunas vai ter cada matriz? '))

mata: [[int]] = [[0 for x in range(n)] for x in range(m)]
matb: [[int]] = [[0 for x in range(n)] for x in range(m)]
matc: [[int]] = [[0 for x in range(n)] for x in range(m)]

print('Digite os valores da matriz A:')
for i in range(m):
    for j in range(n):
        mata[i][j] = int(input(f'Elemento[{i},{j}]: '))

print('Digite os valores da matriz B:')
for i in range(m):
    for j in range(n):
        matb[i][j] = int(input(f'Elemento [{i},{j}]: '))

for i in range(m):
    for j in range(n):
        matc[i][j] = mata[i][j] + matb[i][j]


print('\nMatriz soma:')
for i in range(m):
    for j in range(n):
        print(f'{matc[i][j]} ', end='')
    print()
