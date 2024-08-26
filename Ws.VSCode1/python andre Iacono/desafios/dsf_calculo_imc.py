
peso = float(input('Qual seu peso (Kg): '))
altura = float(input('Qual sua altura (M): '))

imc = peso / (altura ** 2)

resultado = ''
print('~' * 20)
if imc < 18.5:
    resultado = 'Magreza'
elif imc < 25:
    resultado = 'Normal'
elif imc <= 30:
    resultado = 'Sobrepeso'
elif imc < 40:
    resultado = 'Obesidade'
else:
    resultado = 'Obesidade Grave'

print(f'Seu IMC é de {imc:.1f}')
print(f'Seu resultado é considerado como {resultado}')
