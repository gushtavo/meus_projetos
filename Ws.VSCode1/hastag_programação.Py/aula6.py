# dicionario
dict_produtos = {'airpod': 2000, 'ipad': 9000, 'iphone': 6000, 'macbook': 11000}

#pegar um elemento
print(dict_produtos['macbook'])

#editar um elemento
dict_produtos['iphone'] = dict_produtos['iphone'] * 1.3
print(dict_produtos)

#quatidade de itens
print(len(dict_produtos))

#retirar um item do dicionario
# dict_produtos.pop('airpod')
# print(dict_produtos)

#adicionar um item no dicionario
dict_produtos['apple watch'] = 2500
print(dict_produtos)

#verificar se um item existe no dicionario
if 'iphone' in dict_produtos:
    print('Existe Produto')
else:
    print('Não existe')

#verificar se um valor existe nos valores do dicionario
if 9000 in dict_produtos.values():
    print('Existe valor')
else:
    print('Não existe valor')

nome_produto = input('Nome do Produto: ').lower()
preco_produto = float(input('Preço do Produto: '))

# cadastra o novo produto(caso ele não existir)
# caso o produto exita ele vai editar o produto
dict_produtos[nome_produto] = preco_produto
print(dict_produtos)

# além disso: o programa no final tem que atualizar os preços de todos os produtos
#os novos valores  que são 10% a mais do que o preço original

# for produto in dict_produtos:
#     novo_preco = dict_produtos[produto] * 1.1   # ensinado na video aula
#     dict_produtos[produto] = novo_preco
# print(dict_produtos)

# meu jeito
for item, aumento in dict_produtos.items():
    novo_preco = aumento + (aumento * 0.1)
    dict_produtos[item] = novo_preco

print(dict_produtos)
