# num = 1

# while num <= 10:
#     print(num)
#     if num == 5:
#         break
#     num += 1

# for num in range(1, 11):
#     if num == 5:
#         print('Pulei')
#         continue
#     print(num)


# frutas = ['maça', 'uva', 'laranja', 'maça', 'morango', 'limão', 'maça']

# qtd_maca = 0
# for fruta in frutas:
#     if fruta == 'maça':
#         qtd_maca += 1

# print(f'Tem {qtd_maca} Maça na lista')

# numero = float(input('Digiote um numero: ').strip())

# if numero <= 10:
#     print('Numero é menor ou igual a 10')
# elif numero > 10:
#     print('Numero é maior que 10')


# idade = int(input('Digite sua idade: ').strip())

# if idade <= 13:
#     print('Você é uma criança')
# elif idade <= 19:
#     print('Você é um adolescente')
# else:
#     print('Você é um Adulto')


# carros = ['BMW X6', 'BMW I5', 'BMW I8']

# carro_usuario = input('Digite o carro que você deseja: ').strip().upper()

# if carro_usuario in carros:
#     print('Este carro está disponível')
# else:
#     print('Desculpe, este carro não está disponível')


# while True:
#     fruta = input('Digite uma fruta: ').strip().lower()

#     if fruta == 'abacate':
#         break
# print('Parabens, você acertou a fruta!')

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in lista:
#     if num % 2 == 0:
#         print(f'O número {num} é par')
#     else:
#         print(f'O número {num} é ímpar')

# cidades = ('são paulo', 'rio de janeiro', 'porto alegra')

# user_cidade = input('Digite uma cidade: ').strip().lower()

# if user_cidade in cidades:
#     print('A cidade está na lista de cidades')
# else:
#     print('A cidade não está na lista de cidades')

# pais = {
#     'brasil': 'brasilia',
#     'italia': 'roma',
#     'inglaterra': 'londres',
#     'frança': 'paris',
#     'espanha': 'madrid'
# }

# user_pais = input('Digite um país: ').strip().lower()
# if user_pais in pais:
#     print(f'A capital de {user_pais.title()} é {pais[user_pais].title()}')
# else:
#     print('Não temos informações da capital desse País')


# amigos1 = {'Lucas', 'Luiza', 'Eduarda', 'Kaique', 'Julia'}
# amigos2 = {'Erika', 'Julia', 'Marcela', 'Amanda', 'Luiza'}

# amigos_em_comum = amigos1.intersection(amigos2)
# print(amigos_em_comum)


# def ao_guadrado(x):
#     return x ** 2


# user_numeros = int(input('digite um numero: ').strip())
# print(f'O Quadrado de {user_numeros} é {ao_guadrado(user_numeros)}')
