notafinal: float

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

notafinal = nota1 + nota2

print('NOTA FINNAL = {:.1f}'.format(notafinal))
if notafinal < 60.0:
    print('REPROVADO!')
else:
    print('APROVADO!')
