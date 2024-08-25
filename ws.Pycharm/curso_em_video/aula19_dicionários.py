#dados = dict()
#dados = {'nome':'pedro', 'idade':25, 'sexo':'F'}
#dados['sexo'] = 'M' #adicionar item
#del dados['idade'] #remover item
'''pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 19}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #exibir items do dicionario
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'Goerge Lucas'}
print(filme.values()) #exibir valores
print(filme.keys()) #exibir chaves
print(filme.items()) #exibir chaves e valores
for k, v in filme.items():
    print(f'O {k} é {v}')
filme1 = {'titulo': 'Avengers',
          'ano': 2012,
          'diretor': 'Joss Whewdon'}
filme2 = {'titulo': 'Matrix',
          'ano': 1999,
          'diretor': 'Wachowski'}
locadora = []
locadora.append(filme)
locadora.append(filme1)
locadora.append(filme2)
for i, v in enumerate(locadora):
    print(f'{locadora[i]['titulo']}')
print(locadora[1]['diretor'])
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])'''
estado = {}
brasil = []
for c in range(3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    print(f'UF: {e['uf']} sigla: {e['sigla']}')
    for v in e.values():
        print(v, end=' ')
    print()
