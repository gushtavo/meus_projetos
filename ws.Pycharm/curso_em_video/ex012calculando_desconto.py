preco = float(input('Qual e o preço do produto: R$'))

desc = preco - (preco * 5 / 100.0)

print(f'O produro que custava R${preco:.2f}, na promoção de 5% vai custar R${desc:.2f}')
