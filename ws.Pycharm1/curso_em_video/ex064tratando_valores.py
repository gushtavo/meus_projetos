soma = 0
cont = 0
num = int(input('Digite um valor [999 para PARA]: '))
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digite um valor [999 para PARAR]: '))
print(f'Soma dos Valores: {soma}')
print(f'Total de números digitados: {cont}')
