escala = input('Voce vai digitar a temperatura em qual escala (C/F): ')

if escala == 'F':
    fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))

    celsius = 5.0 / 9.0 * (fahrenheit - 32)
    print('temperatura equivalente em Celsius: {:.2f} C'.format(celsius))
elif escala == 'C':
    celsius = float(input('Digite a temperatura em Celsius: '))

    fahrenheit = celsius * 9.0 / 5.0 + 32
    print(f'Temperatura equivalente em Fahrenheit {fahrenheit:.2f} F')