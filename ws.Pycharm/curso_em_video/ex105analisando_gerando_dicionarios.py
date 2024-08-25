def notas(* num, sit=False):
    """
    ->Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    print('~' * 30)
    dados = {}
    dados['Total'] = len(num)
    dados['Maior'] = max(num)
    dados['Menor'] = min(num)
    soma = 0
    for s in num:
        soma += s
    dados['Média'] = soma / len(num)
    #dados['Média'] = sum(num) / len(num)
    if sit:
        if dados['Média'] < 5:
            dados['Situação'] = 'Ruim'
        elif dados['Média'] < 7:
            dados['Situação'] = 'Razoável'
        else:
            dados['Situação'] = 'Boa'
    return dados


resp = notas(6, 8.8, 5.6, 7.5, sit=True)
#print(resp)
help(notas)
