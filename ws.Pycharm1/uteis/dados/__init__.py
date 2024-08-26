def leiaDinheiro(preco):
    while True:
        valor = str(input(preco)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO! "{valor}" é um preço Inválido!\033[m')
        else:
            return float(valor)


def leiaint(num):
    while True:
        try:
            valor = int(input(num).strip())
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um Número Inteiro Válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mERRO!O Usuário Preferiu não Digitar esse Número.\033[m')
            return 0
        else:
            return valor


def leiafloat(num):
    while True:
        try:
            valor = float(input(num).strip())
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número Real Válido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse Número.\033[m')
            return 0
        else:
            return valor

