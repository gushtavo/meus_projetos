r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segemntos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmento acima NÃO PODEM FORMAR um triângulo!')
