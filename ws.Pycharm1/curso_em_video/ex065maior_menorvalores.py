soma = cont = maior = menor = 0
continuar = ''
while continuar in 'S':
    num = int(input('Digite um número: '))
    soma = soma + num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continuar = input('Quer continuar (S/N): ').strip().upper()
media = soma / cont
print(f'Você digitou {cont} números e média foi {media:.2f}')
print(f'O maior valor foi {maior} e menor foi {menor}')
