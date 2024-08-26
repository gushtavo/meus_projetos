def leiaint(num):
    while True:
        try:
            valor = int(input(num).strip())
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um Número Inteiro Válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO!O Usuário Preferiu não Digitar esse Número.\033[m')
            return 0
        else:
            return valor


def linha(tam=42):
    return '~' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua Opção:\033[m ')
    return opc
