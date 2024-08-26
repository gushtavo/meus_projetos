num = int(input('Digite um numero: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[31m', end='')
    print(i, end=' ')
print(f'\n\033[mO numero {num} foi Divisível {total} vezes')
if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
