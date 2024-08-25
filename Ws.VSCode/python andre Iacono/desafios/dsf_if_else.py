temp = input('Qual a temperatura da carne: ')
temp = int(temp)

if temp < 48:
    print('cozinhar por mais alguns minutos')
elif 48 <= temp < 54:
    print('Selada')
elif temp < 60:
    print('Ao ponto para o mal')
elif temp < 65:
    print('Ao ponto')
elif temp < 71:
    print('Ao ponto para bem')
elif temp < 77:
    print('Bem passada')
else:
    print('Você queimou a carne!')
