soma = 0
nome_maisvelho = ''
maisvelho = 0
mulhermenor = 0
for i in range(4):
    print('=' * 5, end='')
    print(f' {i + 1}ª PESSOA ', end='')
    print('=' * 5)
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo (F/M): ').upper().strip()
    soma += idade
    if i == 0 and sexo == 'M':
        maisvelho = idade
        nome_maisvelho = nome
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nome_maisvelho = nome
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
media = soma / 4
print(f'\nA media de idade do grupo é de {media:.1f} anos')
print(f'O homen mais velho é {nome_maisvelho} e tem {maisvelho} anos')
print(f'Ao todo são {mulhermenor} com menos de 20 anos.')
