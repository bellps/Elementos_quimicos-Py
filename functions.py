import requests
from googletrans import Translator

def retorna_dados_elemento(elemento,search):
    if search=="atomicname":
        elemento = traduzir(elemento, "en")

    response = requests.get('https://neelpatel05.pythonanywhere.com/element/{}?{}={}'.format(search, search, elemento))
    dados_elemento = response.json()
    return dados_elemento

def traduzir(texto,lg):
    translator = Translator()
    en = translator.translate(texto, dest=lg)
    return en.text
