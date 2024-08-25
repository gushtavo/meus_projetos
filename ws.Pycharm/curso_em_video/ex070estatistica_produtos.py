print('-' * 30)
print('{:^30}'.format('LOJA USE CENTERS'))
print('-' * 30)
total = mais_demil = barato = cont = 0
produto_barato = ''
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if cont == 1:
        barato = preco
        produto_barato = produto
    else:
        if preco < barato:
            barato = preco
            produto_barato = produto
    if preco > 1000:
        mais_demil += 1
    continua = input('Quer continuar (S/N): ').strip().upper()[0]
    while continua not in 'SN':
        continua = input('Quer continuar (S/N): ').strip().upper()[0]
    if continua[0] == 'N':
        break
print('{:=^31}'.format(' FIM DO PROGRAMA '))
print(f'O valor Total gasto na compra foi de R${total:.2f}')
print(f'Temos {mais_demil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} que custa R${barato:.2f}')
