numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
'''num = int(input('Digite um número entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Você digitou o Número {numeros[num]}')'''
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num > 20 or num < 0:
        num = int(input('Tente Novamente. Digite um numero entre 0 e 20: '))
    print(f'Você digitou o Número {numeros[num]}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar (S/N): ').strip().upper()[0]
    if continuar[0] in 'N':
        break
