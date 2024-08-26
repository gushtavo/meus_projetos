valor: float

minutos = int(input('Digite a quantidade de minutos: '))

valor = 50.0

if minutos > 100:
    valor = valor + (minutos - 100) * 2.0
    print(f'VALOR A PAGAR: R${valor:.2f}')
else:
    print('VALOR A PAGAR: R${:.2f}'.format(valor))
