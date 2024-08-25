n = int(input('qual a ordem da matriz: '))

mat: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = float(input(f'Elemento [{i},{j}]: '))

soma = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]

print(f'\nSoma dos elementos positivos: {soma:.1f}')

linha = int(input('\nEscolha uma linha: '))
print('LINHA ESCOLHIDA: ', end='')
for i in range(n):
    print(f'{mat[linha][i]} ', end='')

coluna = int(input('\n\nEscolha uma coluna: '))
print('COLUNA ESCOLHIDA: ', end='')
for i in range(n):
    print(f'{mat[i][coluna]} ', end='')

print('\n\nDiagonal Principal: ', end='')
for i in range(n):
    print(f'{mat[i][i]} ', end='')

for i in range(n):
    for j in range(n):
        if mat[i][j] < 0:
            mat[i][j] = mat[i][j] ** 2.0
print('\n\nMATRIZ ALTERDA:')
for i in range(n):
    for j in range(n):
        print(f'{mat[i][j]} ', end='')
    print()
