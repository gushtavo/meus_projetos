num = int(input('Digite um número para'
                '\nCalcular seu fatorial: '))
i = num
fatorial = 1
print(f'Calculando {num}! = ', end='')
while i > 0:
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    fatorial = fatorial * i
    i -= 1
print(fatorial)
