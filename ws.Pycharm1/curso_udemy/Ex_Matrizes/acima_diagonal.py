n = int(input('qual a ordem da matriz: '))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

somaacima = 0
for i in range(n):
    for j in range(n):
        if i < j:
            somaacima = somaacima + mat[i][j]

print(f'\nSoma dos elementos acima da diagonal principal = {somaacima}')
