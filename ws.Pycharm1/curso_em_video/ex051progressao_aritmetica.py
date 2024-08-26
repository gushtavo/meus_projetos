termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a Razão dessa Progressão: '))
decimo = termo + (11 - 1) * razao
for i in range(termo, decimo, razao):
    print(i, end=' -> ')
print('ACABOU')
