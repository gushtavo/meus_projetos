media: float
cont: int; soma: int

print('Digite as idades:')
x = int(input())

if x < 0:
    print('IMPOSSIVEL CALCULAR')
else:
    soma = 0
    cont = 0
    while x >= 0:
        cont = cont + 1
        soma = soma + x
        x = int(input())

    media = soma / cont

    print(f'MEDIA = {media:.2f}')

