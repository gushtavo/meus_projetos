print('Gerador de PA')
print('-=' * 10)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
pa = termo
while cont <= 10:
    print(pa, end=' -> ')
    pa = pa + razao
    cont += 1
print('FIM')
