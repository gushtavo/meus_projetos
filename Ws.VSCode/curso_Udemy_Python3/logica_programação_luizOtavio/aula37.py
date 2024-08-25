# repetições
# while (enquanto)
# Executa uma ação enquanto a condição for verdadeira
# Loop infinito -> quando um codigo não tem fim

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('nao vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 30:
        print(f'Nao vou mostrar {contador}')
        continue

    print(contador)

    if contador == 40:
        break
