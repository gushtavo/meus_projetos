n = int(input('quantos valores vai ter cada vetor: '))

veta: [int] = [0 for x in range(n)]
vetb: [int] = [0 for x in range(n)]
vetc: [int] = [0 for x in range(n)]

print('Digite os valores do vetor A:')
for i in range(n):
    veta[i] = int(input())

print('Digite os valores do vetor B:')
for i in range(n):
    vetb[i] = int(input())

for i in range(n):
    vetc[i] = veta[i] + vetb[i]

print('VETOR RESULTANTE:')
for i in range(n):
    print(f'{vetc[i]}')
