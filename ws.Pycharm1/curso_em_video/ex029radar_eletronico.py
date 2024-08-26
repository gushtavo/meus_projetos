km = float(input('Qual a velocidade atual do carro: '))
if km <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (km - 80) * 7
    print(f'MULTADO! Voce excedeu o limite permitido que é de 80Km/h'
          f'\nVoce deve pagar uma Multa de R${multa:.2f}!')
    print('Dirija com segurança!')
