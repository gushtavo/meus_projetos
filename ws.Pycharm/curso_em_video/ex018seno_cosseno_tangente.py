import math

angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo} tem a TANGENTE de {tangente:.2f}')
