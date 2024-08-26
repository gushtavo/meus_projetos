#x = 'oi'
#print(x) #Erro Semantico de Significado/Exeção NameError

#n = int(input('numero: '))
#print(f'Voce digitou o numero {n}') #ValueError

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por Zero.')
except KeyboardInterrupt:
    print('O Usuário prefiriu não informar os dados.')
except Exception as erro:
    print(f'O Problema Encrontado Foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado')#ZeroDivisionerror

#r = 2 / '2' #TypeError

#lst = [3, 6, 4]
#print(lst[3]) #IndexError KeyError

#import uteis #ModuloNotFoundError
