from datetime import date
ano_atual = date.today().year
dados = {}
dados['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    #faltam = (dados['contratação'] + 35) - ano_atual
    #dados['aposentadoria'] = dados['idade'] + faltam #minha_versão
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - ano_atual)
print('=-' * 30)
print(dados)
for k, v in dados.items():
    print(f' - {k.upper()} tem valor {v}')
