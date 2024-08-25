# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['maria', 'helena', 'eduarda']
tupla = ('python', 'é', 'legal')

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# a, b, c = lista
# print(a, c)
# print(*lista)
# print(*string)
# print(*tupla)
print(*salas, sep='\n')
