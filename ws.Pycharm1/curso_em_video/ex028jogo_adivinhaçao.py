import random
from time import sleep
print('-=-' * 20)
print('Vou pensar em numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
comp = random.randint(0, 5)
voce = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if comp == voce:
    print('PARABENS! voce conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no numero {comp} e nao no {voce}!')
