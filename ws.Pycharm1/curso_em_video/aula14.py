n = 1
par = 0
impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 != 0:
        impar += 1
    elif n != 0:
        par += 1
print('ACABOU')
print(f'{par} são numeors pares e {impar} são numeros impares.')
