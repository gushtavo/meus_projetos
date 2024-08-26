m = int(input('quantas linhas vai ter a matriz ? '))
n = int(input('quantas colunas vai ter a matriz ? '))

mat: [[int]] = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    for j in range(0, n):
        mat[i][j] = int(input('elemento [{:d} , {:d}]: '.format(i, j)))

print()
print('MATRIZ DIGITADA:')
for i in range(0, m):
    for j in range(0, n):
        print(f'{mat[i][j]} ', end='')
    print()
