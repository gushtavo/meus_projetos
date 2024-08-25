n = int(input('Digiete um numero para ver sua tabuada: '))

for i in range(1, 11):
    produto = n * i
    print(f'{n} X {i:2} = {produto}')
