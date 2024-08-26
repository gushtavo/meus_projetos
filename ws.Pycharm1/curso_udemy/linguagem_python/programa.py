nome1: str; nome2: str; sexo: str
salario1: float; salario2: float
idade: int

nome1 = input('nome da primeira pessoa: ')
salario1 = float(input('salario da primeira pessoa: '))

nome2 = input('nome da segunda pessoa: ')
salario2 = float(input('salario da segunda pessoa: '))

idade = int(input('digite uma idade: '))
sexo = input('digite um sexo (F/M): ')

print(f'NOME1 : {nome1}')
print(f'SALARIO1 : {salario1:.2f}')
print()
print(f'NOME2 : {nome2}')
print(f'SALARIO2 : {salario2:.2f}')
print()
print('IDADE = {:d}'.format(idade))
print('SEXO = {:s}'.format(sexo))