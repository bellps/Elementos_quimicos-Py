import json
from requests import get
from googletrans import Translator
from prettytable import PrettyTable
from os import system

dados = {}

def traduzir(texto, lg):
    translator = Translator()
    en = translator.translate(texto, dest=lg)
    return en.text

def tabelaSimples(elemento, search):
    global dados
    system('cls')

    dados = dadosElemento(elemento, search)

    tabela_simples = PrettyTable(['Característica','Valor'])
    tabela_simples.align['Característica'] = "l"

    tabela_simples.add_row(["Símbolo:", dados['symbol'], ])
    tabela_simples.add_row(["Número atômico:", dados['atomicNumber'], ])
    tabela_simples.add_row(["Massa:",  dados['atomicMass']])
    tabela_simples.add_row(["Grupo:", traduzir(dados['groupBlock'], "pt")])
    tabela_simples.add_row(["Estado físico:", traduzir(dados['standardState'], "pt")])

    print("\n{}".format(tabela_simples.get_string(title=traduzir(dados['name'], "pt"))))

def tabelaCompleta():
    global dados

    option = input("\nDeseja ver a tabela completa, em inglês, desse elemento? (S/N)\n")
    
    if option.lower() == 's':
        tabela_completa = PrettyTable(['Technical features','Values'])
        tabela_completa.align['Technical features'] = "l"

        for keys,values in dados.items():
            tabela_completa.add_row([keys, values])
        
        print("\n{}".format(tabela_completa.get_string(title=dados['name'])))

    elif option.lower() == 'n':
        pass

    else:
        print("Opção inválida")
        return tabelaCompleta()

def dadosElemento(elemento, search):
    if search == "atomicname":
        elemento = traduzir(elemento, "en")

    response = get('https://neelpatel05.pythonanywhere.com/element/{s}?{s}={e}'.format(s=search, e=elemento))
    dados_elemento = response.json()

    return dados_elemento

def continuar():
    option = input("\nDeseja fazer outra consulta (S/N)?\n")

    if option.lower() == "n":
        return False
    elif option.lower() == "s":
        system('cls')
        return True
    else:
        print("Opção não encontrada.")
        return continuar()
