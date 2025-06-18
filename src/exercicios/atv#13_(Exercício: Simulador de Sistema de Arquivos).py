"""Módulo para atividade #13 de Estrutura de Dados.
O sistema permitirá adicionar/atualizar produtos, buscar 
produtos por código e exibir o estoque completo, tudo isso 
utilizando uma Árvore Binária de Busca (BST) implementada de 
forma "funcional" (sem classes) e um menu interativo para o usuário
"""
def criar_no_bst(valor_codigo_id, valor_qtdd): #função 1
    return {
        'codigo_id' : valor_codigo_id,
        'quantidade' : valor_qtdd,
        'esquerda' : None,
        'direita' : None
    }

def inserir_produto_bst(raiz_bst, valor_codigo_id, valor_qtdd): #função 2
    if raiz_bst is None:
        return criar_no_bst(valor_codigo_id, valor_qtdd)

    if valor_codigo_id == raiz_bst['codigo_id']:
        raiz_bst['quantidade'] += valor_qtdd
    elif valor_codigo_id < raiz_bst['codigo_id']:
        raiz_bst['esquerda'] = inserir_produto_bst(raiz_bst['esquerda'], valor_codigo_id, valor_qtdd)
    else:
        raiz_bst['direita'] = inserir_produto_bst(raiz_bst['direita'], valor_codigo_id, valor_qtdd)
    
    return raiz_bst

def buscar_produto_bst(raiz_bst, valor_codigo_id): #função 3
    if raiz_bst is None:
        return None
    
    if valor_codigo_id == raiz_bst['codigo_id']:
        return raiz_bst['quantidade']
    elif valor_codigo_id < raiz_bst['codigo_id']:
        return buscar_produto_bst(raiz_bst['esquerda'], valor_codigo_id)
    else:
        return buscar_produto_bst(raiz_bst['direita'], valor_codigo_id)

def exibir_estoque_em_ordem_bst(raiz_bst): #função 4
    if raiz_bst is not None:
        exibir_estoque_em_ordem_bst(raiz_bst['esquerda'])
        print(f"Código: {raiz_bst['codigo_id']}, Quantidade: {raiz_bst['quantidade']}")
        exibir_estoque_em_ordem_bst(raiz_bst['direita'])

def verificar_inteiro(valor_inteiro): #tratamento de entrada
    while True:
        try:
            return int(input(valor_inteiro))
        except:
            print(" Erro: somente valores inteiros são aceitos")

def exibir_menu(): #função para chamar o menu
    print("\n ======= Gerenciador de Estoque =======")
    print(" [1] --> Adicionar produto")
    print(" [2] --> Atualizar produto")
    print(" [3] --> Buscar produto por código")
    print(" [4] --> Exibir todos os produtos")
    print(" [5] --> Sair")

raiz_bst = None

while True: #loop principal
    exibir_menu()
    opcao = int(input(" Informe o número referente à sua escolha:"))

    if opcao == 1:
        valor_codigo_id = verificar_inteiro(" Informe o código do novo produto: ")
        valor_qtdd = verificar_inteiro(" Informe a quantidade inicial: ")
        raiz_bst = inserir_produto_bst(raiz_bst, valor_codigo_id, valor_qtdd)
        print(f" Novo produto {valor_codigo_id} adicionado com {valor_qtdd} unidades.")
    
    elif opcao == 2:
        valor_codigo_ido = verificar_inteiro(" Informe o código do produto a atualizar: ")
        valor_qtdd = verificar_inteiro(" Informe a nova quantidade: ")
        raiz_bst = verificar_inteiro(raiz_bst, valor_codigo_id, valor_qtdd)
    
    elif opcao == 3:
        valor_codigo_id = verificar_inteiro(" Informe o código do produto a buscar: ")
        valor_qtdd = buscar_produto_bst(raiz_bst, valor_codigo_id)
        if valor_qtdd is not None:
            print(f" Produto {valor_codigo_id} possui {valor_qtdd} unidades em estoque.")
        else:
            print(f" Produto {valor_codigo_id} não encontrado no estoque.")
    
    elif opcao == 4:
        print("\n ====== Estoque Atual ======")
        if raiz_bst is None:
            print(" Estoque vazio!")
        else:
            exibir_estoque_em_ordem_bst(raiz_bst)
    
    elif opcao == 5:
        print(" Saindo...")
        break
    
    else:
        print(" Erro: escolha uma opção de 1 a 4.")
