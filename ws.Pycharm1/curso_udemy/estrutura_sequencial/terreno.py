area: float; preco: float

largura = float(input('digite a largura do terreno: '))
comprimento = float(input('digite o comprimento do terreno: '))
valor = float(input('digite o valor por metro quadrado: '))

area = largura * comprimento
preco = area * valor

print('Area do terreno = {:.2f}'.format(area))
print(f'Preco do terreno = {preco:.2f}')