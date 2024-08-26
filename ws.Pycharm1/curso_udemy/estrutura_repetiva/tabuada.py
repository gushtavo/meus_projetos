produto: int

n = int(input('Deseja a tabuada para qual valor: '))

for i in range(1, 11):
    produto = n * i
    print(f'{n} X {i} = {produto}')
