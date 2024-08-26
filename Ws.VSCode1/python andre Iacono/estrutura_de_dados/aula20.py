'''
# Unpacking list
'''

produtos = ['arroz', 'feijao', 'laranja', 'maça', 5, 6, 7, 8]

# item1, item2, item3, item4 = produtos

# item1 = produtos[0]
# item2 = produtos[1]
# item3 = produtos[2]
# item4 = produtos[3]

item1, item2, *outros, item3 = produtos
print(item1)
print(item2)
print(item3)
print(outros)
