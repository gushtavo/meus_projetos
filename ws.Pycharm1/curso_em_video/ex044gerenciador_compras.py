print('=' * 10, end='')
print(' LOJA USECENTERS ', end='')
print('=' * 10)
compra = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão''')
pagamento = int(input('Qual a opção: '))
if pagamento == 1:
    desconto = compra - (compra * 10 / 100)
    print(f'Sua compra de R${compra:.2f} vai custar R${desconto:.2f} no final.')
elif pagamento == 2:
    desconto = compra - (compra * 5 / 100)
    print(f'Sua compra de R${compra:.2f} vai custar R${desconto:.2f} no final.')
elif pagamento == 3:
    parcela = compra / 2
    print(f'Sua compra de R${compra:.2f}, será parcelda em 2x de R${parcela:.2f} SEM JUROS.')
elif pagamento == 4:
    qparcela = int(input('Quantas parcelas: '))
    juros = compra + (compra * 20 / 100)
    parcela = juros / qparcela
    print(f'Sua compra será parcelada em {qparcela}x de R${parcela:.2f} COM JUROS')
    print(f'Sua compra de R${compra:.2f} vai custar R${juros:.2f} no final.')
else:
    print(f'Opção INVÁLIDA de pagamento. Tente novamente!')
