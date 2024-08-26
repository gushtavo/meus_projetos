'''
# Try, except
    # Excelente para teste
    # nao para o programa
    # Mensagens customizadas para quando encontrar o erro

# Else e Finally
    else so retorna se o try nao conter nenhum erro
    Finally retorna independente do que aconteça com o Try (True ou False)
     
# Anotações
    indetificar os erros
    Tratar o Erro
    testar partes do codigo
    => continua a executar o codigo mesmo sabendo onde está o erro
'''

# listas

# try:
#     letras = ['a', 'b', 'c']
#     print(letras[3])
# except IndexError:
#     print('Index não existe')

# input

try:
    valor = int(input('Digite o valor do produto: R$ '))
    print(f'R$ {valor:.2f}')
except ValueError:
    print('favor digitar um valor inteiro.')
# finally:
#     print('Codigo Ok')
else:
    print('Codigo está correto!')
    soma = valor * 5
    print(f'R${soma:.2f}')

print('continução do codigo')
