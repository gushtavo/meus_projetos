# calculadora

while True:
    numero1 = input('\nDigite um Numero: ')
    numero2 = input('Digite outro Numero: ')
    operador = input('Digite um operador (+-/*): ')

    numeros_validos = None
    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('\nUm ou Ambos os Números são invalidos')
        continue

    operadores_permitidos = '+-/*'
    resultado = 0

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador not in operadores_permitidos:
        print('\nOperador Digitado não é válido!')
        continue
    else:
        if operador == '+':
            resultado = numero1_float + numero2_float
        elif operador == '-':
            resultado = numero1_float - numero2_float
        elif operador == '/':
            resultado = numero1_float / numero2_float
        else:
            resultado = numero1_float * numero2_float

    print(f'\nRESULTADO: {numero1}'
          f' {operador} {numero2} = {resultado}')

    sair = input('\nQuer sair (SIM ou NÃO): ').upper().startswith('S')

    if sair is True:
        break
