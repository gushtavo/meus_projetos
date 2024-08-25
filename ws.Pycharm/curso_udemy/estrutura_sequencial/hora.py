hora = int(input('digite uma hora do dia: '))
while hora != 0:
    if hora <= 12:
        print('bom dia!')
    elif hora <= 18:
        print('boa tarde!')
    else:
        print('boa noite!')
    hora = int(input('digite uma hora do dia: '))