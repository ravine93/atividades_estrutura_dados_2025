"""Módulo para atividade #5 de Estrutura de Dados.
Sistema administrativo de e-commerce: gerencia produtos (CRUD) via dicionários, 
com cadastro, listagem, edição e exclusão por código único.
"""
import time

#onde todos os produtos serão armazenados em forma de dicionário
lista_produtos = []
print("\n ========== MENU ==========")
while True: #loop_1
    #menu
    print("\n [1] --> Listar produtos")
    print(" [2] --> Cadastrar produto")
    print(" [3] --> Alterar produto")
    print(" [4] --> Excluir produto")
    print(" [5] --> Sair")
    
    opcao = input(" Digite o número correspondente à sua escolha: ")
    print("")
    
    if opcao.isdigit():#isdigit aceita somente numeros inteiros e positivos
        opcao = int(opcao) #escolhi conveter aqui pra se caso for inserido caracter "não-numérico", eu consiga devolver uma mensagem efetivamente informativa
        if opcao < 1 or opcao > 5:
            print(f" ERRO! Opção inválida. {opcao} não correponde a nenhuma escolha disponível.")
        else:
            if opcao == 1:
                print(" Lista de produtos cadastrados")
                if len(lista_produtos) > 0:
                    print(" Saída bruta:")
                    for produto in lista_produtos: #loop_1.1
                        print(f" \n{(produto)}")
                    print(" \nOrganizando lista...\n")
                    time.sleep(1)
                    for produto in lista_produtos:    
                        print(f" Código: {produto['id']}\n Nome: {produto['nome']}\n Descrição: {produto['descricao']}\n Valor: R${produto['valor']:.2f}\n")
                else:
                    print(" Nenhum produto cadastrado!")

            elif opcao == 2:
                novo_prod = {}
                print(" Cadastrar novo produto")                
                id = input(" Informe o código para cadastro do produto: ")
                if not id.isdigit():
                    print(" Código inválido! O valor de ID deve ser um número inteiro e positivo.")
                else:
                    id = int(id)
                    id_existente = False
                    for produto in lista_produtos: #loop_1.2
                        if produto['id'] == id:
                            print(f" ERRO! Valor informado indisponível. {id} já utilizado.")
                            id_existente = True
                        
                    if not id_existente:
                        novo_prod['id'] = id
                        novo_prod['nome'] = input(" Nome do produto: ")
                        novo_prod['descricao'] = input (" Descrição do produto: ")
                        novo_prod['valor'] = float(input(" Quanto custa o produto: R$"))
                        
                        lista_produtos.append(novo_prod)
                        print( "Atualizando sistema...")
                        time.sleep(2)
                        print(f" Produto {novo_prod['nome']} cadastrado no ID {novo_prod['id']} com sucesso!")

            elif opcao == 3:
                print(" Alterar produto")
                id_up_prod = input(" Informe o ID do produto a ser alterado: ")
                if not id_up_prod.isdigit():
                    print(" ERRO: código inválido! ID deve ser um numero inteiro e positivo.")
                else:
                    id_up_prod = int(id_up_prod)
                    prod_selecionado = None
                    for produto in lista_produtos:
                        if produto['id'] == id_up_prod:
                            prod_selecionado = produto
                            
                    if prod_selecionado:    
                        print(" Informe S para SIM e N para NÃO")
                        decisao_nome = input(" Gostaria de alterar o nome do produto? (S/N)")
                        if decisao_nome.upper() == 'S':
                            prod_selecionado['nome'] = input(" Atualizar nome para: ")
                        elif decisao_nome.upper() == 'N':
                            print(f" Nome '{prod_selecionado['nome']}' mantido!")
                        else:
                            print(" ERRO: Opção inválida!")
                        decisao_desc = input(" Gostaria de alterar a descrição do produto? (S/N)")
                        if decisao_desc.upper() == 'S': 
                            prod_selecionado['descricao'] = input(" Atualizar descritivo para: ")
                        elif decisao_desc.upper() == 'N':
                            print(f" Descrição '{prod_selecionado['descricao']}' mantida!")
                        else:
                            print(" ERRO: Opção inválida!")
                        decisao_valor = input(" Gostaria de alterar o valor do produro? (S/N)")
                        if decisao_valor.upper() == 'S':
                            prod_selecionado['valor'] = float(input(" Atualizar valor para: R$"))
                        elif decisao_valor.upper() == 'N':
                            print(f" Valor '{prod_selecionado['valor']}' mantido!")
                        else:
                            print(" ERRO: Opção inválida!")
                        
                        print(" Atualizando sistema...")
                        time.sleep(2)
                        print(f" Produto {prod_selecionado['nome']} atualizado!")
                    else:
                        print(" ERRO! Não há produto cadastrado com este ID.")

                        
            elif opcao == 4:
                print(" Excluir produto")                
                id_del_prod = input(" Informe o código de cadastro do produto a ser excluído: ")
                if not id_del_prod.isdigit():
                    print(" ERRO: código inválido! Deve ser um numero inteiro e positivo.")
                else:
                    id_del_prod = int(id_del_prod)
                    remover_prod = False
                    for produto in lista_produtos:
                        if produto['id'] == id_del_prod:
                            lista_produtos.remove(produto) #ele me sugere tentar remover com o índice... mas ainda não consegui pq remover pelo índice é melhor do que como fiz
                            print(f" {produto['nome']} foi removido do sistema")
                            remover_prod = True
                        else: 
                            print(" ERRO: Produto com este código (ID) não encontrado!")
            elif opcao == 5:
                print(" Saindo...")
                break
        
            else:
                print(" ERRO: Opção inexistente. Opções válidas: 1 ao 5!")
    else:
        print(" ERRO: As opções são limitadas somente a números inteiros!")