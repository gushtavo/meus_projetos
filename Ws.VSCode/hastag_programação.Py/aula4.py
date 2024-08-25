#if logica e condições

#if condição/comparação:
        # tudo que acontece se a condição for verdadeira
#else:
        # tudo que acontece se a condição for falsa

# > maior que
# < menor que
# >= maior ou igual
# <= menor ou igual
# == igual
# != diferente

vendas = 1500
meta = 1300

if vendas > meta:
    print('vendedor ganha Bonus')
    print('Bateu a meta de vendas')
    bonus = 0.1 * vendas
    print(f'Bonus do vendedor: {bonus}')
else:
    print('Vendedor nao ganha bonus')
    print('Não bateu a meta de vendas')

print('Acabou o programa')

# 2ª cenario
vendas = 2300
vendas_empresa = 25000
meta_empresa = 20000
meta1 = 1300 #ganhar 10%
meta2 = 2000 #ganhar 13%

if vendas >= meta2 and vendas_empresa >= meta_empresa:
    bonus = 0.13 * vendas
elif vendas >= meta1 and vendas_empresa >= meta_empresa:
    bonus = 0.1 * vendas
else:
    bonus = 0

print(f'Bonus: {bonus:.2f}')

listas_produtos = ['airpod', 'iphone', 'ipad', 'macbook']
produto_procurado = input('Digite o nome do produto: ').lower()

if produto_procurado in listas_produtos:
    print('produto no estoque')
else:
    print('Não temos esse produto')