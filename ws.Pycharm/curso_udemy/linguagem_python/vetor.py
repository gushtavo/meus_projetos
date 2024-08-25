n: int
n = int(input('quantos numeros voce vai digitar: '))
vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input('digite um numero: '))

print()
print('NUMEROS DIGITADOS:')
for i in range(0, n):
    print(f'{vet[i]:.1f} ', end='')
