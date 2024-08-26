num = int(input('Digite um numero: '))
print(f'A tabuada de {num} é...')
for i in range(1, 11):
    produto = num * i
    print(f'{num} X {i:2} = {produto}')
