soma: float; mdia: float

n = int(input('Quantos casos voce vai digitar: '))

for i in range(n):
    print('Digite tres numeros:')
    valor = float(input())
    valor1 = float(input())
    valor2 = float(input())

    soma = valor + valor1 + valor2
    media = (valor * 2.0 + valor2 * 3.0 + valor2 * 5.0) / 10.0

    print(f'MEDIA = {media:.1f}')
