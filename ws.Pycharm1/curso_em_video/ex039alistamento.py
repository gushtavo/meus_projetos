from datetime import date

sexo = input('Digite seu sexo: ').upper()
if sexo == 'FEMININO':
    print('O alistamento militar não é obrigatorio para pessoas do sexo feminino.')
elif sexo == 'MASCULINO':
    nascimento = int(input('Ano de nascimento: '))
    ano = date.today().year
    idade = ano - nascimento
    print(f'Quem nasceu em {nascimento} tem {idade} ano(s) em {ano}.')
    if idade < 18:
        faltam = 18 - idade
        print(f'Ainda falta(m) {faltam} anos para o alistamento')
        print(f'Seu alistamento será em {ano + faltam}.')
    elif idade > 18:
        passou = idade - 18
        print(f'Você já deveria ter se alistado há {passou} ano(s).')
        print(f'Seu alistamento foi em {ano - passou}.')
    elif idade == 18:
        print('Você tem que se alistar IMEDIATAMENTE!')
