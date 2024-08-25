# Interpolação básica de strings
# s - Strings
# d e i - int
# f - float
# x e x - Hexadecimal (abdcef0123456789)

nome = 'gustavo'
preco = 1000.95897643
variavel = '%s o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %i é %04X' % (1500, 1500))
