x: int
soma: int

n = int(input('quantos numeros voce vai digitar: '))

soma = 0
for i in range(0, n):
    x = int(input('digite um numero: '))
    soma = soma + x

print(f'SOMA = {soma}')