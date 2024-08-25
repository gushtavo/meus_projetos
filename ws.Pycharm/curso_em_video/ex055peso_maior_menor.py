pesmaior = 0
pesmenor = 0
for i in range(5):
    peso = float(input(f'Peso da {i + 1}ª pessoa: '))
    if i == 0:
        pesmaior = peso
        pesmenor = peso
    else:
        if peso > pesmaior:
            pesmaior = peso
        if peso < pesmenor:
            pesmenor = peso
print(f'O maior peso lido foi {pesmaior:.2f}Kg')
print(f'O menor peso lido foi {pesmenor:.2f}Kg')
