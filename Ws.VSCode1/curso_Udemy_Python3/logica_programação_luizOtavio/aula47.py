# exercicio jogo palavra secreta
# Faça um jogo para o usuário adivinhar qual
# a palavra secreta.
# - Você vai propor uma palavra secreta
# qualquer e vai dar a possibilidade para
# o usuário digitar apenas uma letra.
# - Quando o usuário digitar uma letra, você
# vai conferir se a letra digitada está
# na palavra secreta.
#     - Se a letra digitada estiver na
#     palavra secreta; exiba a letra;
#     - Se a letra digitada não estiver
#     na palavra secreta; exiba *.
# Faça a contagem de tentativas do seu
# usuário.
import os

texto = 'perfume'
letra_acertadas = ''
tentativas = 0
while True:
    letra = input('Digite uma letra: ').strip().lower()
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma Letra.')
        continue

    if letra in texto:
        letra_acertadas += letra

    palavra_formada = ''
    for letra_secreta in texto:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'\nPALAVRA FORMADA: {palavra_formada.upper()}')

    if palavra_formada == texto:
        os.system('cls')
        print('\nPARABENS VOCÊ GANHOU!')
        print(f'A palavra secreta era: {texto}')
        print(f'Tentativas: {tentativas}x')
        letra_acertadas = ''
        tentativas = 0
