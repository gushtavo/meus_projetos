from random import randint
from time import sleep

print('Sou seu Computador...')
print('Acabei de pensar em numero de 0 à 10.')
print('Será que voce consegue adivinhar qual foi?')
comp = randint(0, 10)
voce = int(input('Qual é seu Palpite? '))
print('PROCESSANDO...')
sleep(2)
tentativa = 1
while comp != voce:
    print(f'Computador pensou no numero {comp}')
    voce = int(input('Número ERRADO. tente novamente: '))
    print('PROCESSANDO...')
    sleep(2)
    comp = randint(0, 10)
    tentativa += 1
print(f'Você ACERTOU! o número é {voce} e precisou de {tentativa} Tentativas!')
