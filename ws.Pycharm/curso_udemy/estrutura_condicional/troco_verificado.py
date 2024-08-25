troco: float; faltam: float

preco = float(input('Preço unitario do produto: '))
qtd = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: '))

if preco * qtd > dinheiro:
    faltam = preco * qtd - dinheiro
    print('DINHEIRO INSUFICIENTE. FALTAM R${:.2f} Reais.'.format(faltam))
elif preco * qtd < dinheiro:
    troco = dinheiro - preco * qtd
    print(f'TROCO: R${troco:.2f}')
