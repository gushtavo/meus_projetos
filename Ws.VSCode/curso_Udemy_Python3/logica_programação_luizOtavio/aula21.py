# Operadores Logícos
# and (e), or (ou), not (não)
# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado Falso,
# a expressão inteira será avaliada naquele valor
# são considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar ou [S]air: ').upper()
# senha_digitada = input('Digite sua senha: ')

# senha_permitida = '123456'
# if entrada == 'E' and senha_digitada == senha_digitada:
#     print('Entrar')
# else:
#     print('Sair')

# avaliação de curto circuito
print(True and False and True)

if 0 and 1:
    print(True and 1)
