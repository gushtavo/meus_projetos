m = int(input('Qual a quantidade de linhas da matriz? '))
n = int(input('Qual a quantidade de colunas da matriz? '))

mat: [[float]] = [[0 for x in range(n)] for x in range(m)]
vet: [float] = [0 for x in range(n)]
for i in range(m):
    print(f'Digite os elementos da {i+1}a. linha: ')
    for j in range(n):
        mat[i][j] = float(input())

for i in range(m):
    soma = 0
    for j in range(n):
        soma = soma + mat[i][j]

    vet[i] = soma

print('Vetor gerado:')
for i in range(m):
    print(f'{vet[i]:.1f}')
