sexo = input('Digite seu sexo (F/M): ').strip().upper()
while sexo not in 'MF':
    sexo = input('DADOS INVÁLIDOS. Por Favor, informe seu sexo: ').strip().upper()
print(f'Sexo {sexo} registrado com sucesso')