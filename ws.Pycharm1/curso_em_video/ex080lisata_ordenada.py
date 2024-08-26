valores = list()
for cont in range(0, 5):
    v = int(input('Digite um valor: '))
    if cont == 0 or v > valores[-1]:
        valores.append(v)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos, v)
                print(f'Adiocionado na posição {pos} da lista...')
                break
            pos += 1
print('=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
