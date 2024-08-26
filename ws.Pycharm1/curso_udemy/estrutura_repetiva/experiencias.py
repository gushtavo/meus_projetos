n = int(input('Quantos casos voce vai digitar: '))

rato: float; sapo: float; coelho: float
total: float
rato = 0
sapo = 0
coelho = 0
for i in range(0, n):
    qtdc = int(input('Quantidaes de cobaias: '))
    tipo = input('Tipo da cobaia: ')

    if tipo == 'R':
        rato = rato + qtdc
    elif tipo == 'S':
        sapo = sapo + qtdc
    else:
        coelho = coelho + qtdc

total = rato + sapo + coelho
prato = (rato / total) * 100
psapo = (sapo / total) * 100
pcoelho = (coelho / total) * 100

print()
print('RELATORIO FINAL:')
print(f'TOTAL: {total} cobaias')
print('Total de ratos: {:.1f}'.format(rato))
print(f'Total de sapo: {sapo:.1f}')
print(f'Total de coelhos: {coelho:.1f}')
print(f'Percenrual de ratos: {prato:.2f}%')
print(f'Percentual de sapos: {psapo:.2f}%')
print(f'percentual de coelho: {pcoelho:.2f}%')
