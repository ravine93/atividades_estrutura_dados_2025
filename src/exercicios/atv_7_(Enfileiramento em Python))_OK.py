"""Módulo para atividade #7 de Estrutura de Dados.
Menu interativo para manipulação de fila (enqueue, dequeue, first, last) com loop.  
Implementa operações básicas de fila (FIFO) sem usar deque.  
"""
import time

fila = []
tam_max = int(input(" Informe o tamanho máximo da fila: ")) #pra acelerar resolvi já nem dar lado pro usuário inserir valores 'não-numericos' e que não fossem inteiros

def enfileirar(elemento): #elemento sempre é adicionado ao final da fila, assim como em pilhas
    if len(fila) < tam_max:
        fila.append(elemento)
        print(f" Elemento {elemento} enfileirado com sucesso!")
        return elemento
    else:
        print(" ERRO: Fila cheia!")
        return None

def desenfileirar(): #remove o primeiro elemento que foi inserido
    if len(fila) > 0: # O 0 aqui é tamanho e não índice
        elemento = fila.pop(0) #índice 0 = ínicio
        print(f" Elemento {elemento} desenfileirado!")
        return elemento
    else:
        print(" ERRO: Fila vazia!")
        return None

def primeiro_fila(): #retorna o primeiro elemento da fila
    if len(fila) > 0:
        return fila[0]
    else:
        print(" ERRO: fila vazia!")

def ultimo_fila(): #retorna o último elemento da fila
    if len(fila) > 0: 
        return fila[-1] #return com slice para selecionar o conteúdo do último índice

def isFull(): #se o tamanho (len) da fila for igual ao tam_max, a fila está cheia
    if len(fila) == tam_max: 
        return isFull

def isEmpty(): #se o tamanho(len) da fila for igual a 0, a fila está vazia
    if len(fila) == 0:
        return isEmpty

while True:
    print("\n ========= MENU =========\n")
    print(" [1] --> Enfileirar elemento")
    print(" [2] --> Desenfileirar")
    print(" [3] --> Verificar primeiro da fila")
    print(" [4] --> Verificar último da fila")
    print(" [5] --> Verificar se está cheia")
    print(" [6] --> Verificar se está vazia")
    print(" [7] --> Sair")
    print(" Solução limitada à números inteiros e positivos\n")
    
    opcao = input(" Escolha uma opção: ")
    
    if opcao == '1':
        elemento = int(input(" Digite o elemento a enfileirar: "))
        enfileirar(elemento)
    
    elif opcao == '2':
        desenfileirar()
    
    elif opcao == '3':
        primeiro = primeiro_fila()
        if primeiro:
            print(f" Primeiro elemento: {primeiro}")
    
    elif opcao == '4':
        ultimo = ultimo_fila()
        if ultimo:
            print(f" Último elemento: {ultimo}")
    
    elif opcao == '5':
        if isFull():
            print(f" Fila cheia! A fila {fila} já atingiu o limite de {tam_max} de elementos")
        else:
            print(" ERRO: Fila não está cheia")
    
    elif opcao == '6':
        if isEmpty():
            print(" Fila vazia!")
        else:
            print(f" Fila não está vazia, ela está armazenando: {fila}")
    
    elif opcao == '7':
        print("Saindo...")
        time.sleep(0.5)
        break
    
    else:
        print("Opção inválida! Tente novamente.")
    
    time.sleep(0.5)  # Pequena pausa para melhor visualização
