import functions as f
from unicodedata import normalize

print('\nBem vindo ao "Ache seu Elemento!" As opçõs de busca são:')
while True:
    print("+----------------------------------+\n|1| Procurar pelo nome do elemento |\n|2| Procurar pelo número atômico   |\n|3| Procurar pelo símbolo          |\n+----------------------------------+\n|4| Sair                           |\n+----------------------------------+\n")
    option = int(input("Digite a opção de consulta: "))

    if option==1:
        elemento = (input("Digite o nome do elemento: "))
        search = "atomicname"

    elif option==2:
        elemento = int((input("Digite o número atômico do elemento: ")))
        search = "atomicnumber"

    elif option==3:
        elemento = (input("Digite o símbolo do elemento: "))
        search = "symbol"

    elif option==4:
        break

    else:
        print("Opção inválida!")
        continue

        dados = f.retorna_dados_elemento(elemento,search)
        nome = f.traduzir(dados['name'],"pt")
        grupo = f.traduzir(dados['groupBlock'],"pt")
        estado = f.traduzir(dados['standardState'],"pt")

    try:
        print("\n+-----------------------------------------------------+")
        print("Elemento escolhido: {} \nSímbolo do elemento: {} \nNúmero atômico: {} \nMassa atômica: {} \nGrupo: {} \nEstado físico na temperatura ambiente: {}".format(nome, dados['symbol'], dados['atomicNumber'], dados['atomicMass'], grupo, estado))
        print("+-----------------------------------------------------+")

    except Exception:
        print("|              Elemento não encontrado                |")
        print("+-----------------------------------------------------+")

    finally:
        continuar = input("\nDeseja fazer outra consulta?\n")
        continuar = normalize('NFKD', (continuar.lower())).encode('ASCII', 'ignore').decode('ASCII')

        if continuar == "nao":
            break
        elif continuar == "sim": 
            pass
        else:
            print("Opção não encontrada. Reiniciando aplicação.")

        
        