cadastro = dict()
lista_total = list()

while True:
    try:
        cadastro.clear()
        cadastro['nome'] = str(
            input('Nome do Funcionario(a): ')).strip().title()
        cadastro['idade'] = int(input('Idade do Funcionario(a): '))
        lista_total.append(cadastro.copy())
    except:
        print('ERRO! Informações incorretas.')
    while True:
        quer_cont = input('Quer continuar (S/N): ').upper().strip()
        if quer_cont[0] in 'SN':
            break
    if quer_cont[0] in 'N':
        break

for funcionario in lista_total:
    print(f'NOME: {funcionario['nome']} IDADE: {funcionario['idade']}')
