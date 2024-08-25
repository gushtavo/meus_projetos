# while - loop

# dia = 1
# valor = 100
# while valor > 20:
#     print(f'Dia {dia} Produto em promoção no valor de R${valor:.2f}')
#     dia += 1
#     valor -= 5


valor = input('Digite o valor do produto: ')
valor = int(valor)
comissão = valor + (valor * 0.1)

while valor > 20:
    print('O Valor do produto de R$'
          f'{valor:.2f} será publicado no valor de R${comissão:.2f}')
    break
