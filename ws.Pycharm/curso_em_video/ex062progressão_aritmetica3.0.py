print('Gerador de PA')
print('-=' * 10)
termo = int(input('Primero termo: '))
razao = int(input('Razão da PA: '))
pa = termo
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{pa} -> ', end='')
        pa = pa + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
