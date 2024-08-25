'''
print('Olá mundo Python!')

nome = 'Gustavo'
idade = 19
print(f'Olá meu nome é {nome} e eu tenho {idade} anos.')

num1 = 10
num2 = 3.5
r = num1 / num2
print(r)
'''

'''
nome = input('Qual seu nome: ')
idade = int(input('Qual sua idade: '))

print(f'Olá, {nome}! Você tem {idade} anos.')
'''

'''
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
exponenciacao = num1 ** num2

print(f'Soma: {soma:.2f}')
print(f'Subtração: {subtracao:.2f}')
print(f'Multiplicação: {multiplicacao:.2f}')
print(f'Divisão: {divisao}')
print(f'Exponenciação: {exponenciacao:.2f}')
'''

'''
frutas = ['Morango', 'Uva', 'Maça', 'Melancia', 'Banana']

frutas[1:3] = ['limão', 'Abacate']
frutas[1] = 'Limão'
frutas.append('Laranja')
frutas.insert(1, 'Manga')
frutas.remove('Maça')
del frutas[4]

for fruta in frutas:
    print(f'Eu gosto de {fruta}')

for num in range(1, 11):
    print(num)
'''

'''
frutas = ['Morango', 'Uva', 'Maça', 'Melancia', 'Banana']
vegetais = ['Abobora', 'Batata', 'Cenoura', 'Pimentão', 'Beterraba']

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)'
'''

'''
num = 1
while num <= 10:
    print(num)
    num += 1
'''
