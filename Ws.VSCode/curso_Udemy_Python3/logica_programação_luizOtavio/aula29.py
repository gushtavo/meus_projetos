# introdução try/except
# try - tentar executar o código
# except - ocorreu algum erro ao tentar executar

numero_str = input('Vou dobrar o numero que você digitar: ')

try:
    print('Str:', numero_str)
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.0f}')
# else:
#     print('Isso não é um numero')
