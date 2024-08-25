casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o valor do seu salario: R$'))
anos = int(input('Quantos anos de financiamento: '))
mensal = casa / (anos * 12)
if mensal > salario * 30 / 100:
    print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${mensal:.2f}')
    print('EMPRÉSTIMO NEGADO!')
else:
    print(f'EMPRÉSTIMO pode ser CONCEDIDO! O valor da mensalidade será de R${mensal:.2f}')
