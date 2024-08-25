from random import shuffle

alu1 = input('primeiro aluno: ')
alu2 = input('segundo aluno: ')
alu3 = input('terceiro aluno: ')
alu4 = input('quarto aluno: ')
lista = [alu1, alu2, alu3, alu4]
shuffle(lista)
print('A ordem da apresentação sera:')
print(f'{lista}')
