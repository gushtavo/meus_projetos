# Operadores Logícos
# and (e), or (ou), not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado veradeiro,
# são considerados falsy (que você já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

# entrada = input('[E]ntrar ou [S]air: ').upper()
# senha_digitada = input('Digite sua senha: ')

# senha_permitida = '123456'
# if entrada == 'E' or entrada == 'e' and senha_digitada == senha_digitada:
#     print('Entrar')
# else:
#     print('Sair')

# avaliação de curto circuito
print(0 or False or 0 or 'abc' or True)
senha = input('Senha: ') or 'sem senha'
print(senha)

if 0 and 1:
    print(True and 1)
