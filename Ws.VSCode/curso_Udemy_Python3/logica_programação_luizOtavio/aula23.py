# operador Logico "not"
# Usado para interver expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')

print(not True)  # False
print(not False)  # True
