num = [2, 5, 9, 1]
# num[2] = 3 #altera_valor
num.insert(0, 7)  # acrescenta_lista
print(num)
# num.append(15) #acrescenta_lista
# num.sort(reverse=True) #organiza_reversa
# num.sort() #organiza
# num.pop(3) #remova_index
# num.pop() #remova_ultimo_index
# del num[2] #remova_index
# num.remove(5) #remova_valor
'''if 5 in num:
    num.remove(5)
else:
    print('Não achei o numero 5')
print(num)
print(f'Esta lista tem {len(num)} elementos')'''
'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)'''
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for pos,v in enumerate(valores):
    print(f'Na posição {pos} encontrei o {v}!')
print('Cheguei ao final da lista.')'''
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
