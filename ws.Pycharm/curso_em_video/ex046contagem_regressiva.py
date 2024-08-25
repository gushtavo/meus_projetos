from time import sleep

print('-=' * 10, end='')
print(' VIRADA DO ANO! ', end='')
print('-=' * 10)
for i in range(10, -1, -1):
    sleep(1)
    print(i)
sleep(1)
print('FELIZ ANO NOVO!!!')
