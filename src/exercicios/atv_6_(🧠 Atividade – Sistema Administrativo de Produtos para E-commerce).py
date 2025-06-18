"""Módulo para atividade #5 de Estrutura de Dados.
Capaz de cadastrar, listar, alterar e excluir dados de
dicionários contidos em uma lista
"""
import time

i = -1 #pilha vazia
tam_max = int(input(" Informe o tamanho máximo da pilha: ")) #5
pilha = [] #mais dinâmico do que *tam_max

def push_empilhar(elemento):
    global i
    if i < tam_max -1: #i = -1 e tam_max = 5, então enquanto i for menor que 5, um elemento será adicionado / tam_max -1 pois nesta var se inicia com 1 e não com 0 como na variável i
        i = i + 1
        pilha.append(elemento) #método 'append' adiciona o elemento à lista "pilha"
        return elemento

def pop_desempilhar():
    global i
    elemen_del = [] #armazenar elementos removidos
    if i >= 0: #lembrando, contagem inicia do 0
        elemento = pilha.pop() #método 'pop' remove o último elemento adicionado à pilha
        elemen_del.append(elemento)
        i = i -1 #decrementação conforme elemento é deletado
        return elemen_del

def top_pilha():
    if len(pilha) > 0: #se o tamanho da pilha maior que 0
        return pilha[-1] #-1 retorna o último valor da lista

def isFull_pilha():
    if len(pilha) == tam_max: #se tamanho da pilha for o mesmo do valor limite inserido pelo usuário
        return isFull_pilha

def isEmpty_pilha(): 
    if len(pilha) == 0: #se tamanho da pilha for vazio
        return isEmpty_pilha

def removeAll_pilha():
    global i, pilha
    pilha_del = []
    while len(pilha) > 0:
        pilha_del.append(pilha.pop()) #enquanto há a remoção, eu crio uma lista para funcionar como lixeira
    i = -1 #como estou usando o método pop, que elimina elemento por elemento, preciso garantir que o índice reduza conforme os elementos são removidos
    return removeAll_pilha

def mostrar_pilha():
    if isEmpty_pilha():
        print(" Pilha vazia!")
    else:
        print(" Pilha:", pilha)

while True:
    print("\n ========= MENU =========\n")
    print(" [1] --> Empilhar (Push)")
    print(" [2] --> Desempilhar (Pop)")
    print(" [3] --> Verificar topo (Top)")
    print(" [4] --> Verificar se está cheia (isFull)")
    print(" [5] --> Verificar se está vazia (isEmpty)")
    print(" [6] --> Remover todos os elementos (RemoveAll)")
    print(" [7] --> Mostrar pilha")
    print(" [8] --> Sair")
    
    opcao = input("Escolha uma opção: ")
    print("")
    
    if opcao == '1':
        elemento = (input("Digite o número inteiro que será empilhado: "))
        if not elemento.isdigit():
            print(" ERRO! Valor inválido")
        else:   
            if i < tam_max -1: #pq o i começa em -1 
                numero = int(elemento)
                push_empilhar(numero)
            else:
                print(" ERRO: Pilha já está cheia")

    elif opcao == '2':
        elemento = pop_desempilhar()
        if elemento is not None:
            print(f"Elemento desempilhado: {elemento}")
        else:
            print(" ERRO: pilha vazia!")

    elif opcao == '3':
        elemento = top_pilha()
        if elemento is not None:
            print(f"Elemento no topo: {elemento}")
        else:
            print(" ERRO: pilha vazia!")

    elif opcao == '4':
        if isFull_pilha():
            print(f"A pilha está cheia! Ela possui o valor limite de {tam_max} e já está alocando: {pilha}")
        else:
            print("A pilha não está cheia")
    
    elif opcao == '5':
        if isEmpty_pilha():
            print("A pilha está vazia!")
        else:
            print(f"A pilha não está vazia, ja possui {len(pilha)} elemento(s)")
    
    elif opcao == '6':
        removeAll_pilha()
        print(f" Pilha esvaziada: {pilha} ")
    
    elif opcao == '7':
        print(" Mostrando pilha: ")
        time.sleep(0.5)
        mostrar_pilha()
    
    elif opcao == '8':
        time.sleep(1)
        print("Saindo...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
