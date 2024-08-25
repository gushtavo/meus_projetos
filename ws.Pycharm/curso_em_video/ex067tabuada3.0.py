while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    print('=' * 20)
    if num < 0:
        break
    for i in range(1, 11):
        produto = num * i
        print(f'{num} X {i} = {produto}')
    print('=' * 20)
print('PROGRAMA DE TABUADA ENCERRADO. volte sempre!')
