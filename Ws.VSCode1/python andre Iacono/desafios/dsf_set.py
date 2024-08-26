

funcionarios = ['Ana', 'Marcos', 'Alice',
                'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


tem_carro_noite = set(turno_noite) & set(tem_carro)
print(tem_carro_noite)

tem_carro_dia = set(turno_dia) & set(tem_carro)
print(tem_carro_dia)

nao_tem_carro = set(funcionarios) - set(tem_carro)
print(nao_tem_carro)
