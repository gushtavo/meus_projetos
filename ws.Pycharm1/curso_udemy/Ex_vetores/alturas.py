n = int(input('quantas pessoas serao digitadas: '))

altura: [float] = [0 for x in range(n)]
nome: [str] = [0 for x in range(n)]
idade: [int] = [0 for x in range(n)]

soma = 0
for i in range(0, n):
    print(f'DADOS DA {i+1}a pessoa:')
    nome[i] = str(input('NOME: '))
    idade[i] = int(input('IDADE: '))
    altura[i] = float(input('ALTURA: '))
    soma = soma + altura[i]

media = soma / n
print('ALTURA MEDIA: {:.2f}'.format(media))
# (cont * 100) / n
cont = 0
for i in range(0, n):
    if idade[i] < 16:
        cont = cont + 1

porc = (cont * 100) / n
print(f'Pessoas com menos de 16 anos: {porc:.2f}%')
for i in range(0, n):
    if idade[i] < 16:
        print(f'{nome[i]}')
