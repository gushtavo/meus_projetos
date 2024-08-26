n = int(input('quantos elementos vai ter o vetor: '))

vet: [int] = [0 for x in range(n)]

for i in range(n):
    vet[i] = int(input('Digite um numero: '))

soma = 0
npares = 0
for i in range(n):
    if vet[i] % 2 == 0:
        soma = soma + vet[i]
        npares = npares + 1

media = soma / npares
if soma == 0:
    print('NENHUM NUMERO PAR')
else:
    print(f'MEDIA DOS PARES = {media:.1f}')