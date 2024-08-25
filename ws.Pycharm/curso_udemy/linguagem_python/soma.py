x: int
soma: int

x = int(input('digite um numero: '))

soma = 0
while x != 0:
    soma = soma + x
    x = int(input('digite outro numero: '))

print('Soma = {:d}'.format(soma))
