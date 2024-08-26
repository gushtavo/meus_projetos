print('Digite dois numeros inteiros:')
x = int(input())
y = int(input())

print()
if x % y == 0 or y % x == 0:
    print('SAO MULTIPLOS!')
else:
    print('NAO SAO MULTIPLOS!')
