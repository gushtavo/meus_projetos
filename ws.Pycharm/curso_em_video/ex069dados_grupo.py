qtdpessoa = qtdhomem = qtdmulhermenos_20 = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('-' * 40)
    idade = int(input('IDADE: '))
    sexo = input('Sexo (F/M): ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('Sexo (F/M): ').strip().upper()[0]
    print('-' * 40)
    if idade > 18:
        qtdpessoa += 1
    if sexo in 'M':
        qtdhomem += 1
    if sexo in 'F' and idade < 20:
        qtdmulhermenos_20 += 1
    continuar = input('Quer continuar (S/N): ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Quer continuar (S/N): ').strip().upper()[0]
    if continuar[0] == 'N':
        break
    print('-' * 40)
print('=' * 30)
print(f'Total de pessoas com mais de 18 anos: {qtdpessoa}')
print(f'Ao todo temos {qtdhomem} homens cadastrados')
print(f'E temos {qtdmulhermenos_20} Mulheres com menos de 20 anos.')
