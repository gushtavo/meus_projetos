lista = [[], []]
num = 0
for n in range(0, 7):
    num = int(input(f'Digite o {n + 1}º. Valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    if num % 2 != 0:
        lista[1].append(num)
print('=-' * 30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores Ímpares digitados foram: {lista[1]}')
