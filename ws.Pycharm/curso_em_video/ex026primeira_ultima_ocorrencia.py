frase = input('Digite uma frase: ').strip().upper()
print(f'A letra "A" aparece {frase.count('A')} vezes na frase')
print(f'A primeira letra "a" aparece na posiçao {frase.find('A')+1}')
print(f'A ultima letra "a" aparece na posição {frase.rfind('A')+1}')
