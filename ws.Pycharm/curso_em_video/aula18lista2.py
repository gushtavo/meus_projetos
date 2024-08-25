'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
'''galera = [['Gustavo', 34], ['Maria', 23], ['Ana', 15], ['jose', 56]]
#print(galera[2][0])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''
galera = []
dados = list()
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0].upper()} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0].upper()} é menor de idade.')
        menor += 1
print(f'temos {maior} maiores e {menor} menores de idade.')
