from time import sleep
num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))
operacao = False
while not operacao:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print(f'O resultado de {num1} + {num2} é {soma}')
    elif opcao == 2:
        multiplicacao = num1 * num2
        print(f'O resultado de {num1} X {num2} é {multiplicacao}')
    elif opcao == 3:
        maior = 0
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        operacao = True
    else:
        print('Opção Inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre !')
