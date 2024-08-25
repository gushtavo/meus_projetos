n = int(input('quantos numeros voce vai digitar: '))

vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input('Digite um numero: '))

maior = vet[0]
posmaior = 0
for i in range(0, n):
    if vet[i] > maior:
        maior = vet[i]
        posmaior = i

print(f'MAIOR VALOR = {maior:.1f}')
print('POSICAO DO MAIOR VALOR = {:d}'.format(posmaior))
