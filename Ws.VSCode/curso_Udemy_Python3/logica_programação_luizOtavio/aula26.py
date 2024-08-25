# formatação básica de strings
# s - string
# d - int
# f - float
# . < numeros de digitos > f
# x ou X - hexadecimal
# (caractere)( > <^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - forca o numero a aparecer antes dos zeros
# sinal - + ou -
# ex.: 0 > -100, .1f
# conversion Flags - !r !s !a __repr__ __str__

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}.')
print(f'{variavel:^10}.')
print(f'{1000.87324:0>+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:04X}')
print(f'{variavel!a}')
