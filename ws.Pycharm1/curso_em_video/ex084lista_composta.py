pessoas = []
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (Kg): ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = (str(input(f'Quer continuar (S/N): '))).strip().upper()[0]
    if continuar[0] in 'N':
        break
print('=-' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
for p in pessoas:
    print(f'{p[0].upper()} ', end='')
print(f'\nO maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0].upper()} ', end='')
print(f'\nO menor peso foi de {menor:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0].upper()} ', end='')
