# exercicio
# Faça uma lista de comprar com listas
# O usuário deve ter a possibilidade de
# inserir, apagar e listar valores da sua lista
# Não permita que o programa quebre com
# erros de índices inexistentes na lista.
import os


lista_produto = list()
while True:
    try:
        print('Selecione uma Opção')
        opcao = input('[i]inserir [a]apagar [l]listar: ').strip().lower()

        if opcao == 'i':
            produto = input('Produto: ')
            lista_produto.append(produto)

        if opcao == 'a':
            indice = input('Escolha um indice para apagar: ').strip()
            todos_indices = []
            for i, produto in enumerate(lista_produto):
                todos_indices.append(i)

            indice = int(indice)
            if indice in todos_indices:
                del lista_produto[indice]
            else:
                print('Não foi possivel apagar esse indice')
                continue

        if opcao == 'l':
            os.system('cls')
            if len(lista_produto) == 0:
                print('Não a nada para listar')
            else:
                for i, produto in enumerate(lista_produto):
                    print(i, produto)

    except:
        print('ERRO!')
        continue
