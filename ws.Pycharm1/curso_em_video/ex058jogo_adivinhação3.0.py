from random import randint
print('''Sou seu computador...
Acabei de pensar em número de 0 a 10.
Será que você consegue adivinhar qual foi?''')
comp = randint(0, 10)
voce = int(input('Qual seu palpite? '))
tentativa = 1
while comp != voce:
    if voce < comp:
        print('Mais...Tente mais uma vez.')
    else:
        print('Menos...Tente mais uma vez.')
    voce = int(input('Qual seu palpite? '))
    tentativa += 1
print(f'Eu pensei em {comp}')
print(f'Você Acertou com {tentativa} Tentativas. PARABÉNS!')
