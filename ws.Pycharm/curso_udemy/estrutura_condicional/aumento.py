aumento: float; novosalario: float
porcetagem: int

salario = float(input('Digite o salario da pessoa: '))

if salario <=1000.0:
    porcetagem = 20
    aumento = salario * porcetagem / 100
    novosalario = salario + aumento
elif salario <= 3000.0:
    porcetagem = 15
    aumento = salario * porcetagem / 100
    novosalario = salario + aumento
elif salario <= 8000.0:
    porcetagem = 10
    aumento = salario * porcetagem / 100
    novosalario = salario + aumento
else:
    porcetagem = 5
    aumento = salario * porcetagem / 100
    novosalario = salario + aumento

print('NOVO SALARIO = R${:.2f}'.format(novosalario))
print(f'AUMENTO = R${aumento:.2f}')
print('PORCENTAGEM = {:d}%'.format(porcetagem))
