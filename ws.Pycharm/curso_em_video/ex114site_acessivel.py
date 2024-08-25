import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://g1.globo.com/sp/sao-paulo/')
except urllib.error.URLError:
    print('O site não está acessível no momento')
else:
    print('Consegui acessar o Site com sucesso')
    #print(site.read())
