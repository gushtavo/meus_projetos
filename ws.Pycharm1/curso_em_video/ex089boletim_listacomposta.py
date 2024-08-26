ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = input('Quer continuar (S/N): ').strip().upper()[0]
    if continuar[0] in 'N':
        break
print('=-' * 30)
print(ficha)
print(f'{"nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0].upper():<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    mostrar = int(input('Mostrar notas de qual aluno. (999 interrompe): '))
    if mostrar == 999:
        print('FINALIZANDO...')
        break
    if mostrar <= len(ficha) - 1:
        print(f'Notas de {ficha[mostrar][0]} são {ficha[mostrar][1]}')
print('<<<<< Volte Sempre! >>>>>')
