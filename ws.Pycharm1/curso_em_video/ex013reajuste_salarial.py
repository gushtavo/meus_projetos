sal = float(input('Qual o salario do Funcionario? R$'))
aum = sal + (sal * 15 / 100.0)

print(f'Um funcionario que ganhava R${sal:.2f}, com 15% de aumento passará a receber R${aum:.2f}.')
