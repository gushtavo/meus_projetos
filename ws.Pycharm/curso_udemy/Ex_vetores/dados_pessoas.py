n = int(input('quantas pessoas serao digitadas: '))

altura: [float] = [0 for x in range(n)]
genero: [str] = [0 for x in range(n)]

for i in range(n):
    altura[i] = float(input(f'Altura da {i+1}a pessoa: '))
    genero[i] = input(f'Genero da {i+1}a pessoa: ')

soma = 0
nmulher = 0
cont = 0
for i in range(n):
    if genero[i] == 'F':
        soma = soma + altura[i]
        nmulher = nmulher + 1
    else:
        cont = cont + 1
media = soma / nmulher

maior = altura[0]
menor = altura[0]
for i in range(n):
    if altura[i] > maior:
        maior = altura[i]
    elif altura[i] < menor:
        menor = altura[i]

print(f'MAIOR ALTURA: {maior:.2f}')
print(f'NENOR ALTURA: {menor:.2f}')
print(f'MEDIA DAS ALTURAS DAS MULHERES: {media:.2f}')
print(f'NUMEROS DE HOMENS: {cont}')
