n = int(input('quantos voce vai digitar: '))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input('Digite um numero: '))
cont = 0
print('NUMEROS PARES:')
for i in range(0, n):
    if vet[i] % 2 == 0:
        print(f'{vet[i]} ', end='')
        cont = cont + 1

print(f'\nQUANTIDADE DE PARES = {cont}')