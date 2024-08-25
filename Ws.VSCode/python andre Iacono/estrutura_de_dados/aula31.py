'''
# list comprehesion
    # Mais simples de escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressão for iten in itens]
'''
frutas1 = ['abacaxi', 'abacate', 'uva', 'maça', 'morango', 'banana']
frutas2 = []

for item in frutas1:
    if 'b' in item:
        frutas2.append(item)

# frutas2 = [item for item in frutas1 if 'n' in item]

print(frutas2)

# com numeros

valores = []
for i in range(6):
    valores.append(i * 10)


# valores = [i * 10 for i in range(6)]
print(valores)
