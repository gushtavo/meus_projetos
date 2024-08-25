km = float(input('Qual é a distancia da sua viagem: '))
print('Voce esta pretes a começar uma viagem de {:.1f}Km.'.format(km))
if km > 200:
    preco = km * 0.45
else:
    preco = km * 0.50
print(f'E o preço da sua passagem será de R${preco:.2f}')
