n = int(input('qual a ordem da matriz: '))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]

neg = 0
for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f'elemento [{i},{j}]: '))

print('Diagonal principal:')
for i in range(n):
    print(f'{mat[i][i]} ', end='')

for i in range(n):
    for j in range(n):
        if mat[i][j] < 0:
            neg = neg + 1

print(f'\nQuantidades de negativos: {neg}')
