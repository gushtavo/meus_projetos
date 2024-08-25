#inputs
'''email = input('Escreva seu e-mail: ')
nome = input('Seu Primeiro nome: ')

print(nome, email)

print(f'{nome}, Verifique seu email: {email} que enviamos um link de confirmação!')

faturamento = float(input('Digite o Faturamento: '))
imposto = faturamento * 0.1

print(imposto)'''
#Listas

vendas = [100, 50, 14, 20, 30, 700]

 #soma dos elementos
total_vendas = sum(vendas)
print(total_vendas)

soma = 0
for s in vendas:
    soma += s

print(f'o total de vendas foi {soma}')

#tamanho da lista
quantidades_vendas = len(vendas)
print(quantidades_vendas)

#maximo e minimo
print(max(vendas))
print(min(vendas))

#pegar posição
print(vendas[3])

lista_produtos = ['iphone', 'airpod', 'ipad', 'macbook']

'''produto_procurado = input('Pesquise pelo nome do produto: ').lower()

print(produto_procurado in lista_produtos)'''

# adiocionar um item
lista_produtos.append('apple watch')
print(lista_produtos)

# remover um item
lista_produtos.remove('macbook') # remover pelo nome    
print(lista_produtos)

lista_produtos.pop(0) #remover pelo indice
print(lista_produtos)

# editar um item
precos = [1000, 1500, 3500]
precos[0] = precos[0] * 1.5
print(precos)

# contar quatntas vezes um item aparece na lista
lista_produtos = ['iphone', 'airpod', 'macbook', 'ipad', 'iphone', 'apple watch', 'iphone']
print(lista_produtos.count('iphone'))

# ordenar uma lista
lista_produtos.sort()
print(lista_produtos)

vendas.sort(reverse=True)
print(vendas)
