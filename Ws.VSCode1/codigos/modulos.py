# import os

# lista_arquivos = os.listdir("arquivos")
# print(lista_arquivos)

# for nome_arquivo in lista_arquivos:
#     if "txt" in nome_arquivo:
#         if "22" in nome_arquivo:
#             os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
#         elif "23" in nome_arquivo:
#             os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")

import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
dic_resposta = resposta.json()
# print(dic_resposta)
cotacao_dolar = dic_resposta["USDBRL"]
print(cotacao_dolar["bid"])