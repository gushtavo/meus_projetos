pagamento: float

nome = input('Nome: ')
valor = float(input('Valor por hora: '))
horas = int(input('Hoars trabalhadas: '))

pagamento = valor * horas
print()

print(f'O pagamento para {nome} deve ser de {pagamento:.2f} .')