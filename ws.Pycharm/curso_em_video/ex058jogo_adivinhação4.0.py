from random import randint
print('''Sou seu Computador...
Acabei de pensar em número de 0 10.
Será que você consegue Adivinhar?''')
comp = randint(0, 10)
acertou = False
paltites = 0
while not acertou:
    voce = int(input('Qual seu paltite? '))
    paltites += 1
    if voce == comp:
        acertou = True
    else:
        if voce < comp:
            print('Mais...Tente mais uma vez.')
        else:
            print('Menos...Tente mais uma vez.')
print(f'Acertou com {paltites} Tentativas. PARABÉNS!')
