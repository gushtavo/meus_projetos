n = int(input('Quantos numeros voce vai digitar? '))


dentro = 0
fora = 0
for i in range(0, n):
    x = int(input('Digite um numero: '))
    if x >= 10 and x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print('{:d} DENTRO'.format(dentro))
print(f'{fora} FORA')
