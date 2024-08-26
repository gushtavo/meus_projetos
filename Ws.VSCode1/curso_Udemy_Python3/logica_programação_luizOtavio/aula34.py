# repetições
# while (enquanto)
# Executa uma ação enquanto a condição for verdadeira

condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome.title()}')

    if nome == 'sair':
        break

print('Acabou')
