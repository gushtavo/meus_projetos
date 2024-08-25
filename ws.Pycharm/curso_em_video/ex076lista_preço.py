produtos = ('Lápis', 1.75,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('=' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}R$', end='')
    else:
        print(f'{produtos[pos]:>8.2f}')
