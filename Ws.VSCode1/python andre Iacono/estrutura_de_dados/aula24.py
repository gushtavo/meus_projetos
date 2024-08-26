'''
# tuple (tupla)
    # Armazenar mais de uma informação em variaveis
    # Manter a sequencia dos dados em uma variavel
    # Não podem ser alteradas (Immutable)
'''

cores_list = ['amarelo', 'azul', 'vermelho', 'preto', 'branco']
cores_tuple = ('amarelo', 'azul', 'vermelho', 'preto', 'branco')

print(type(cores_list))
print(type(cores_tuple))

cores_list.append('roxo')

print(cores_list)
print(cores_tuple)
