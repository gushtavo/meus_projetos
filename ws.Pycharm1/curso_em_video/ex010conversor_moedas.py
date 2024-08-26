real = float(input('quanto dinheiro voce tem na carteira: R$'))

euro = 0
dolar = 0
while real != 0:
    moeda = input('Para qual moeda deseja converter (euro/dolar)? ')
    if moeda == 'euro':
        euro = real / 5.34
        print(f'\nCom R${real:.2f} voce pode comprar £{euro:.2f}')
    elif moeda == 'dolar':
        dolar = real / 4.96
        print(f'\nCom R${real:.2f} voce pode comprar US${dolar:.2f}')
    real = float(input('\ndigite novamente: R$'))
