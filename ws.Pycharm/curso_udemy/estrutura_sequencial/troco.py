total: float; troco: float

preco = float(input('Preco unitario do produto: '))
quantidade = int(input('Quantidade comprada: '))
dinheiro = float(input('Dinheiro recebido: '))

total = quantidade * preco
troco = dinheiro - total

print('TROCO: {:.2f}'.format(troco))
