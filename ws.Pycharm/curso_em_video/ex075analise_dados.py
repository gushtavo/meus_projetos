numeros = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores par digitado foram: ', end='')
for pares in numeros:
    if pares % 2 == 0:
        print(pares, end=' ')
