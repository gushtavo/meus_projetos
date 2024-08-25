def area():
    area = largura * comprimento
    print(f'A área de um Terreno {largura:.1f}m x {comprimento:.1f}m é de {area:.1f}m².')


print('  Controle de Terrenos  ')
print('-' * 30)
largura = float(input('Largura (M): '))
comprimento = float(input('Altura (M): '))
area()
