mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        mat[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-' * 20)
for l in range(3):
    for c in range(3):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
print('=-' * 20)
soma = soma_col = maior = 0
for l in range(3):
    for c in range(3):
        if mat[l][c] % 2 == 0:
            soma += mat[l][c]
print(f'A soma dos valores pares é {soma}')
for l in range(3):
    soma_col += mat[l][2]
print(f'A soma dos valores da terceira coluna é {soma_col}')
for c in range(3):
    if c == 0:
        maior = mat[1][c]
    elif mat[1][c] > maior:
        maior = mat[1][c]
print(f'O maior valor da segunda linha é {maior}')
