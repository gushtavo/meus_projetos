# Flags (bandeira) -> Marcar um local
# None -> não Valor
# is e is not -> é ou não é (tipo, valor, identidade)
# id = identidade

condicao = False
passou_no_if = None
if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Não faça algo')

# print(passou_no_if, passou_no_if is None)
# print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')
