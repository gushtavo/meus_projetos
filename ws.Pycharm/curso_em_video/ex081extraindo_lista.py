valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar (S/N): ').strip().upper()[0]
    if continuar[0] in 'N':
        break
print('-=-' * 20)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem Decrescente {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da Lista! na posição {valores.index(5) + 1}.')
else:
    print('O valor 5 não foi encontrado na lista!')