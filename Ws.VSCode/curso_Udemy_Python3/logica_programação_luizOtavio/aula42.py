frase = 'aaaooo'

i = 0
qtd_mais_apareceu = 0
letra_mais_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    quantas_vezes_apareceu = frase.count(letra_atual)

    if qtd_mais_apareceu < quantas_vezes_apareceu:
        qtd_mais_apareceu = quantas_vezes_apareceu
        letra_mais_apareceu = letra_atual

    i += 1

print(f'A letra que mais apareceu foi '
      f'"{letra_mais_apareceu}" {qtd_mais_apareceu} vezes.')
