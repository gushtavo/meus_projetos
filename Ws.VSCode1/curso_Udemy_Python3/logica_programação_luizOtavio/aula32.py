# exercios
# desafio_1

# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

# try:
#     numero_inteiro = int(input('Digite um número Inteiro: '))
#     par = numero_inteiro % 2 == 0
#     impar = numero_inteiro % 2 != 0
#     if par:
#         print(f'O número inteiro {numero_inteiro} é par')
#     if impar:
#         print(f'O número inteiro {numero_inteiro} é ímpar')
# except (TypeError, ValueError):
#     print('O valor digitado não é número inteiro')

# desafio_2

# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
# descrito, exiba a saudação apropriada. Ex.
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

# def leiafloat(msg):
#     while True:
#         try:
#             n = float(input(msg))
#         except (ValueError, TypeError):
#             print('ERROR! Digite um valor válido')
#         else:
#             return n


# while True:
#     horario = leiafloat('Me diga que horas são: ')

#     if horario < 12:
#         print('Tenha um Bom dia !')
#         break
#     elif horario < 18:
#         print('Tenha uma Boa tarde!')
#         break
#     elif horario < 24:
#         print('Tenha uma Boa noite!')
#         break
#     else:
#         print('Por favor digite um horario válido.')

# desafio_3

# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".

while True:
    try:
        nome = input('Digite seu primeiro nome: ').strip()
    except (ValueError, TypeError):
        print('ERRO AO EXECUTAR O PROGRAMA')
    else:
        espaco = nome.count(' ')
        if espaco:
            print('Digite apenas o primeiro nome')
        elif len(nome) <= 4:
            print('Seu nome é curto!')
            break
        elif len(nome) <= 6:
            print('Seu nome é normal!')
            break
        else:
            print('Seu nome é muito grande')
            break
