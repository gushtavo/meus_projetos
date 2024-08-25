ficha = list()
dados = dict()
soma = 0
while True:
    dados.clear()
    dados['nome'] = input('Nome: ')
    while True:
        dados['sexo'] = str(input('Sexo (F/M): ')).strip().upper()[0]
        if dados['sexo'][0] in 'FM':
            break
        print('ERRO! Por favor, Digite apenas F ou M.')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    ficha.append(dados.copy())
    while True:
        continuar = str(input('Quer continuar (S/N): ')).strip().upper()[0]
        if continuar[0] in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar[0] in 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(ficha)} pessoas cadastradas.')
media = soma / len(ficha)
print(f'B) A média das idades é de {media:.2f} anos.')
print('C) As Mulheres cadastradas foram ', end='')
for d in ficha:
    if d['sexo'][0] in 'F':
        print(d['nome'], end=', ')
print('\nD) Lista de pessoas que estão acima da Média:')
for d in ficha:
    if d['idade'] > media:
        for k, v in d.items():
            print(f'   {k} = {v};', end='')
        print()
