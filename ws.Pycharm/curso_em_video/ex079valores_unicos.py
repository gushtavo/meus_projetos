valores = list()
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar (S/N): ').strip().upper()[0]
    if continuar[0] == 'N':
        break
print('=' * 40)
print(f'Você digitou os valores {sorted(valores)}')
