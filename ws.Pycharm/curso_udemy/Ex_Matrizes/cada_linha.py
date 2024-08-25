n = int(input('qual a ordem da matriz: '))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]
maiorlinhas: int = []

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

for i in range(n):
    maior = mat[i][0]
    for j in range(1, n):
        if maior < mat[i][j]:
            maior = mat[i][j]

    maiorlinhas.append(maior)

print('\nmaior elemento de cada linha:')
for i in range(n):
    print(f'{maiorlinhas[i]}')
