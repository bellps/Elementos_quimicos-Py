import functions as f

continuar = True

print('\nBem vindo ao "Ache seu Elemento!" As opçõs de busca são:')
while continuar:
    print("""
    +----------------------------------+
    |1| Procurar pelo nome do elemento |
    |2| Procurar pelo número atômico   |
    |3| Procurar pelo símbolo          |
    +----------------------------------+
    |4| Sair                           |
    +----------------------------------+
    """)

    option = input("Digite a opção de consulta: ")

    if option == '1':
        elemento = (input("Digite o nome do elemento: "))
        search = "atomicname"

    elif option == '2':
        elemento = input("Digite o número atômico do elemento: ")
        search = "atomicnumber"

    elif option == '3':
        elemento = (input("Digite o símbolo do elemento: "))
        search = "symbol"

    elif option == '4':
        break

    else:
        print("Opção inválida!")
        continue


    try:
        f.tabelaSimples(elemento, search)

    except:
        print("""
    +-----------------------------------+
    |      Elemento não encontrado      |
    +-----------------------------------+

Procure pelo elemento novamente: """)
        continue

    else:
        f.tabelaCompleta()
        continuar = f.continuar()
        
