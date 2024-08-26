'''
# sets (listas)
    # similar as listas
    # Evita itens duplicados
    # Não utiliza index
'''

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

# print(num1 | num2)  # Union
# print(num1 - num2)  # Difference
print(num1 ^ num2)  # Simmetric Difference
# print(num1 & num2)  # And


# funções Sets

# s1 = {1, 2, 3, 4, 5, 6}
# s1.add(7)
# s1.update([8, 9, 10, 11])
# s1.remove(10)
# s1.discard(60)

# print(s1)

# sets com strings

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2)
print(set4)
