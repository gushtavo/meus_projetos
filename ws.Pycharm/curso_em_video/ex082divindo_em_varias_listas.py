valores = list()
pares = list()
impar = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in "SN":
        continuar = input('Quer Continuar (S/N): ').strip().upper()[0]
    if continuar[0] in 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=-' * 20)
print(f'A lista completa é {valores}')
print(f'A lista de Pares é {pares}')
print(f'A lista de Ímpares é {impar}')
