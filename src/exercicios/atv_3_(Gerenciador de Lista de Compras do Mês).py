"""Módulo para atividade #3 de Estrutura de Dados.
Gerencia lista de compras: adicionar, remover, verificar itens, 
exibir primeiros/últimos, converter maiúsculas/minúsculas e contar itens. Sai com opção 10.
"""

compras = []
while True:
    print("\n MENU")
    print(" [1] --> Adicionair um novo item à lista.")
    print(" [2] --> Remover um item lista.")
    print(" [3] --> Verificar a existência de um item na lista.")
    print(" [4] --> Mostrar o primeiro item da lista.")
    print(" [5] --> Mostrar o último item da lista.")
    print(" [6] --> Mostrar os 3 primeiros e os 3 últimos itens da lista.")
    print(" [7] --> Colocar todos os itens em letras maiúsculas.")
    print(" [8] --> Colocar todos os itens em letras minusculas.")
    print(" [9] --> Mostrar a quatidade de itens na lista.")
    print(" [10] --> Sair.")

    opcao = int(input("\n Informe o [número] da opção desejada: "))

    if opcao == 1:
        item = input("\n Informe o item a ser adicionado: ")
        if item in compras:
            print(" Item já cadastrado!")
        else:
            compras.append(item)
            print(f" {item} cadastrado com sucesso!")

    elif opcao == 2:
        item = input("\n Informe o item a ser removido: ")
        if item in compras:
            decisao = input(f"Deseja realmente remover o {item} da lista? (s/n)")
            if decisao == 's':
                compras.remove(item)
                print(f" {item} removido com sucesso!")
            elif decisao == 'n':
                print(f" {item} NÃO removido!")
            else:
                print("Erro! Informe somente 's' para sim e 'n' para não!")
        else:
            print(f" {item} não encontrado!")
    
    elif opcao == 3:
        item = input("\n Informe o item a ser consultado: ")
        if item in compras:
            print(f" {item} está cadastrado na lista!")
        else:
            print(f" {item} não encontrado!")

    elif opcao == 4:
        if len(compras) != 0:
            print(f" Primeiro item da lista: {compras[0]}")
        else:
            print(" Lista de compras vazia!")
        
    elif opcao == 5:
        if len(compras) != 0:
            print(f" Último item da lista: {compras[-1]}")
        else:
            print(" Lista de compras vazia!")

    elif opcao == 6:
        if len(compras) != 0 and len(compras) < 6:
            print(" A lista possui menos de 6 itens cadastrados!")
        elif len(compras) >= 6:
            print(f" 3 primeiros itens: {compras[0:3]}\n 3 últimos itens: {compras[-3:]}")
        else:
            print(" Lista de compras vazia!")

    elif opcao == 7:
        if len(compras) != 0:
            for l in compras:
                item = l.upper()
                print(item)
        else:
            print(" Lista de compras vazia!")


    elif opcao == 8:
        if len(compras) != 0:
            for l in compras:
                item = l.lower()
                print(item)

        else:
            print(" Lista de compras vazia!")

    elif opcao == 9:
        if len(compras) != 0:
            print( len(compras))
        else:
            print(" Lista de compras vazia!")

    elif opcao == 10:
        print(" Saindo...\n\n")
        break

    else:
        print("Opção inválida, escolha somente de [1] até [10] !!!")
