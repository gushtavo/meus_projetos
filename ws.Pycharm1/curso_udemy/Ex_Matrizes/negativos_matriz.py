m = int(input('Qual a quantidade de linhas da matriz? '))
n = int(input('Qual a quantidade de colunas da matriz? '))

mat: [[int]] = [[0 for x in range(n)] for x in range(m)]

for i in range(m):
    for j in range(n):
        mat[i][j] = int(input(f'Elementos [{i},{j}]: '))

print('Valores negativos:')
for i in range(m):
    for j in range(n):
        if mat[i][j] < 0:
            print(f'{mat[i][j]}')
