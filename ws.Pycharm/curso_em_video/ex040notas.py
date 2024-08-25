nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if media < 5.0:
    print('O aluno esta REPROVADO!')
elif media < 6.9:
    print('O aluno esta em RECUPERAÇÃO!')
else:
    print('O aluno esta APROVADO!')
