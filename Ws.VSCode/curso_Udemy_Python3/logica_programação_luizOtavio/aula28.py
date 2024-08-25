nome = input('Digite seu nome: ').strip()
idade = input('Digite sua idade: ').strip()
espaco = nome.count(' ')

if nome and idade:
    primeira_letra = nome[0]
    ultima_letra = nome[-1]
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print('Seu nome contém (ou não) Espaços? ', end='')
    if espaco > 0:
        print(f'Sim, {espaco} Espaços')
    else:
        print('Não')
    print(f'Seu nome tem {len(nome) - espaco} Letras.')
    print(f'A primeira letra do seu nome é: {primeira_letra.title()}')
    print(f'A Última letra do seu nome é: {ultima_letra.title()}')
else:
    print('Desculpe, você deixou campos vazios.')
