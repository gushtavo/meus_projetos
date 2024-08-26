
cores = ['amarelo', 'vermelho', 'azul', 'preto', 'branco']

while True:
    cor_cliente = input('Digite a cor Desejada: ').strip()

    if cor_cliente.lower() in cores:
        print('Sim, essa cor está Disponivel')
    else:
        print('Não temos essa cor em estoque')
        break
