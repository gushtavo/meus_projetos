n = int(input('Quantos numeros voce vai digitar: '))

vet: [float] = [0 for x in range(n)]
soma = 0
for i in range(0, n):
    vet[i] = float(input('Digite um numero: '))
    soma = soma + vet[i]

print('\nVALORES = ', end='')
for i in range(0, n):
    print(f'{vet[i]} ', end='')

print(f'\nSOMA = {soma:.2f}')
media = soma / n
print(f'MEDIA = {media:.2f}')
