n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
menor = n1
#verificando menor
if n2 < n3 and n2 < n1:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3
#verificando maior
maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
print(f'O maior numero digitado foi {maior}')
print(f'O menor numero digitado foi {menor}')
