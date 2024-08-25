#for - loop estrutura de repetição

listas_vendas = []
meta = 1200
percentual_bonus = 0.1
funcionarios = int(input('Quantos funcionarios venderam: '))
for i in range(funcionarios):
    vendedor = int(input(f'Vendedor {i + 1}: '))
    listas_vendas.append(vendedor)

print('~' * 30)

for i, venda in enumerate(listas_vendas):
    if venda >= meta:
        bonus = percentual_bonus * venda
    else:
        bonus = 0
    print(f'vendedor {i + 1} Bônus: {bonus}')
