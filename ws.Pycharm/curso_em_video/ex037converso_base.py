num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para Conversão:
[ 1 ] coverter para BINÁRIO
[ 2 ] coverter para OCTAL
[ 3 ] coverter para HEXADECIMAL''')
opcao = int(input('Sua opçao: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. TENTE NOVAMENTE!')
    