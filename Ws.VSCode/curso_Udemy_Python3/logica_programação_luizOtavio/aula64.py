# gerando CPF
from random import randint


nove_digitos = ''
for i in range(9):
    nove_digitos += str(randint(0, 9))

multiplicador_1 = 10
soma_1 = 0
for digito in nove_digitos:
    soma_1 = soma_1 + multiplicador_1 * int(digito)
    multiplicador_1 -= 1

digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(f'O primeiro digito do CPF é: {digito_1}')

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

print(novo_cpf)
