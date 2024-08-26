from datetime import date

ano_atual = date.today().year
menor = 0
maior = 0
for i in range(7):
    nascimento = int(input(f'Em que ano a {i + 1}ª pessoa nasceu: '))
    idade = ano_atual - nascimento
    if idade < 21:
        menor += 1
    else:
        maior = maior + 1
print(f'\n{menor} Pessoas ainda não atingiram a maioridade.')
print(f'{maior} Pessoas já são maiores')
