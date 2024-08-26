# Operadores in  e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# G U S T A V O
# -6 -5 -4 -3 -2 -1 0

# nome = 'gustavo'
# print(nome[3])
# print('gust' in nome)
# print('cinco' in nome)
# print('-' * 10)
# print('avo' not in nome)
# print('gust' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
