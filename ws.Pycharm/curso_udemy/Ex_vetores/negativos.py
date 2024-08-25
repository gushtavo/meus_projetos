n = int(input('Quantos numeros voce vai digitar: '))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input('Digite um numero: '))

print('Numeros negativos:')
for i in range(0, n):
    if vet[i] < 0:
        print(f'{vet[i]}')
