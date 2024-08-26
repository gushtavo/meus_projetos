n = int(input('quantas pessoas voce vai digitar: '))

nome: [str] = [0 for x in range(n)]
idade: [int] = [0 for x in range(n)]

for i in range(n):
    print('DADOS DA {:d}a PESSOA:'.format(i+1))
    nome[i] = input('Nome: ')
    idade[i] = int(input('Idade: '))

maisvelho = idade[0]
pnome = 0
for i in range(n):
    if idade[i] > maisvelho:
        maisvelho = idade[i]
        pnome = i

print(f'PESSOA MAIS VELHA: {nome[pnome]}')
