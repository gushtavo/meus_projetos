'''
# Funções
 DRY - Don't repeat yourself. => não se repita  

parametros e argumentos
argumentos Default e Non-Default
Default = Aquele que voce define o valor no parametro
Non-Default = Aquele que não define o valor no parametro
'''


# def boas_vindas(nome, quantidade):
#     print(f'Olá {nome}!')
#     print(f'Temoas {quantidade} laptops no estoque.')


# boas_vindas('Gustavo', 67)

# Non-Default e Default


# def boas_vindas(nome, quantidade=0):
#     print(f'Olá {nome}!')
#     print(f'Temoas {quantidade} laptops no estoque.')


# boas_vindas('lua')


# PRINT E RETURN


def cliente(nome):
    print(f'Olá {nome}, Tudo bem?')


def cliente1(nome):
    return f'Olá {nome}, tudo bem?'


x = cliente('mireia')
y = cliente1('Ana')
print(x)
print(y)
