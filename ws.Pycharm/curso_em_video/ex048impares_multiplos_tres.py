soma = 0
cont = 0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            soma = soma + i
            cont = cont + 1
print(f'A SOMA de todos os {cont} valores solicitados é {soma}')
