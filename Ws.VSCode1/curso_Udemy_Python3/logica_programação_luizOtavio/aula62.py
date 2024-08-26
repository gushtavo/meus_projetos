# Calculo do segundo dígito do CPF
# CPF: 746.824.890-70
# Colete a soma dos 9 primeiros dígitos do CPF,
# MAIS O PRIMEIRO DIGITO,
# multiplicando cada um dos valores por uma
# contagem regressiva começando de 11

# Ex.:  746.824.890-70 (7468248907)
#    11 10  9  8  7  6  5  4  3  2
# *  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
#    77 40 54 64 14 24 40 36  0 14

# Somar todos os resultados:
# 77+40+54+64+14+24+40+36+0+14 = 363
# Multiplicar o resultado anterior por 10
# 363 * 10 = 3630
# Obter o resto da divisão da conta anterior por 11
# 3630 % 11 = 0
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta

# O segundo dígito do CPF é 0
# CPF '36440847007' # Esse CPF gera o primeiro digito como 10 (0)
try:
    cpf = input('Digite seu CPF: ')
except (ValueError, TypeError):
    print('ERRO! valor Inválido , digite somente numeros.')

# digito_1
nove_digitos = cpf[:9]
multiplicador_1 = 10
soma_1 = 0
for digito in nove_digitos:
    soma_1 = soma_1 + multiplicador_1 * int(digito)
    multiplicador_1 -= 1

digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(f'O primeiro digito do CPF é: {digito_1}')

# digito_2
dez_digitos = nove_digitos + str(digito_1)
multiplicador_2 = 11
soma_2 = 0
for digito in dez_digitos:
    soma_2 = soma_2 + multiplicador_2 * int(digito)
    multiplicador_2 -= 1

digito_2 = (soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(f'O segundo digito do CPF é: {digito_2}')

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == novo_cpf:
    print(f'{novo_cpf} é Válido')
else:
    print('CPF Inválido')
