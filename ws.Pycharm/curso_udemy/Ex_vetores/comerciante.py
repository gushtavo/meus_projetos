n = int(input('Serao digitados dados de quantos produtos? '))

nome: [str] = [0 for x in range(n)]
pcompra: [float] = [0 for x in range(n)]
pvenda: [float] = [0 for x in range(n)]
porclucros: [float] = [0 for x in range(n)]

for i in range(0, n):
    print('Produto {:d}:'.format(i+1))
    nome[i] = input('nome: ')
    pcompra[i] = float(input('Preco de compra: '))
    pvenda[i] = float(input('Preco de venda: '))

for i in range (0, n):
    porclucros[i] = (pvenda[i] - pcompra[i]) / pcompra[i] * 100.00

abaixo = 0
entre = 0
acima = 0
for i in range(0, n):
    if porclucros[i] < 10.00:
        abaixo = abaixo + 1
    elif porclucros[i] < 20.00:
        entre = entre + 1
    else:
        acima = acima + 1

tcompra = 0
tvenda = 0
for i in range(0, n):
    tcompra = tcompra + pcompra[i]
    tvenda = tvenda + pvenda[i]

ltotal = tvenda - tcompra

print('\nRELATORIO:')
print(f'Lucro abaixo de 10%: {abaixo}')
print(f'Lucro entre 10% e 20%: {entre}')
print('Lucro acima de 20%: {:d}'.format(acima))
print(f'Valor Total da Compra: {tcompra:.2f}')
print(f'Valor Total de Venda: {tvenda:.2f}')
print('Lucro Total: {:.2f}'.format(ltotal))
