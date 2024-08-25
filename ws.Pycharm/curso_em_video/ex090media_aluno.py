dados = dict()
dados['nome'] = input('Nome: ')
dados['média'] = float(input(f'Media de {dados['nome']}: '))
if dados['média'] >= 7.0:
    dados['situação'] = 'Aprovado'
elif dados['média'] >= 5.0:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k.upper()} é igual a {v}')
