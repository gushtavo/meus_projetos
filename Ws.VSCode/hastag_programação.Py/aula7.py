# funções
def calcula_imposto_total(preco):
    #imposto
    # Aliquota1 - IR = 0.2, se o preço do produto for ate 2000, acima disso a aliquota é 0.3
    # Aliquota2 - ISS = 0.15
    # Aliquota3 - CSLL = 0.05

    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    imposto_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + imposto_iss + imposto_csll
    return imposto_total

lista_preco = [1500, 1000, 800, 3000]
for produto in lista_preco:
    imposto_total = calcula_imposto_total(produto)
    print(f'Imposto Total sobre o produto de R${produto:.2f}: R${imposto_total:.2f}')

print('~' * 55)

nova_lista_preco = [3000, 5000, 6000, 9000]
for preco in nova_lista_preco:
    imposto_total = calcula_imposto_total(preco)
    print(f'Imposto Total sobre o produto de R${preco:.2f}: R${imposto_total:.2f}')
