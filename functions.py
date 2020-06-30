from requests import get
import json
from googletrans import Translator

def retorna_dados_elemento(elemento,search):
    if search=="atomicname":
        elemento = traduzir(elemento, "en")

    response = get('https://neelpatel05.pythonanywhere.com/element/{s}?{s}={e}'.format(s = search, e = elemento))
    dados_elemento = response.json()

    dados_elemento["distribuicao"] = getDistribuicao(dados_elemento["atomicNumber"])
    return dados_elemento

def traduzir(texto,lg):
    translator = Translator()
    en = translator.translate(texto, dest=lg)
    return en.text

def getDistribuicao(z):
    with open("pyElements\distribuicao.json", "r", encoding='utf8') as read_file:
        distribuicao = json.load(read_file)

    for elemento in distribuicao:
        if int(elemento["numAtomico"]) == z:
            return elemento["distribuicao"]