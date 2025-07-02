"""Módulo para atividade #9 de Estrutura de Dados.
Simula um histórico de navegação com lista encadeada simples.
Permite registrar, listar, remover, limpar e buscar visitas
baseadas em URL e horário.
"""

import time

inicio = None #lista vazia para inicialização

def criar_lista(url, horario): #nó
    return {
        "url": url,
        "horario": horario,
        "prox": None
    }

def acessar_site(): #inicia um novo nó -> opção #1
    global inicio
    url = input("Digite o endereço do site: ")
    horario = input("Digite o horário de acesso: ")
    
    novo = criar_lista(url, horario)

    if inicio is None: #se inicio ainda tiver como valor '= none', ele irá receber o 'novo'
        inicio = novo
    else:
        atual = inicio #se não for 'inicio = none' o site atual é substituido pelo 'novo'
        while atual["prox"] is not None: #aí eu prendo num loop  enquanto a chave prox '!= none', ou seja até o penúltimo nó
            atual = atual["prox"] #quando o nó 'atual' encontrar com um nó em que a chave 'prox' é = none, ele sai do loop while. pois quer dizer que não há mais encadeamentos
        atual["prox"] = novo #saindo do loop while, o nó 'novo' é zerado para a proxima vez que a função for chamada

    print(" Site adicionado ao histórico!")

def mostrar_historico(): #opção #2
    if inicio is None:
        print(" Histórico está vazio!")
        return
    
    print("\n Histórico de Navegação:")
    atual = inicio #garantir que seja mostrado a partir do primeiro site (nó) acessado
    while atual is not None: #como quero imprimir todos os sites não uso "while atual["prox"] is not None:", pois aqui com a especificação da chave 'prox', eu só percorreria atré o penultimo nó
        print(f" - {atual['url']} às {atual['horario']}")
        atual = atual["prox"]

def remover_site(): #opção3
    global inicio
    if inicio is None:
        print(" Histórico está vazio!")
        return

    url = input("Digite o endereço do site a remover: ").strip()

    atual = inicio
    anterior = None #se ele começa do primeiro site, logo não há um site anterior (nó)

    while atual is not None: #se o nó 'atual' for != de 'none'
        if atual["url"] == url: #se o site informado já foi acessado
            if anterior is None: #se o nó 'anterior' = 'none', quer dizer que só há um nó (site acessado)
                inicio = atual["prox"]  #remove o primeiro e que é o site inserido
            else:
                anterior["prox"] = atual["prox"] #chave anterior passa a ser a chave inserida
            print(f" Site '{url}' removido do histórico!")
            return
        anterior = atual #chave anterior passa a ser a chave inserida
        atual = atual["prox"] #chave 'atual' (e agora ainserida pelo user) é substituída pela próxima chave 'atual' -> ele puxa a próxima chave para subescrever a chave informada

    print(f" Site '{url}' não encontrado no histórico.")

def limpar_historico(): #opção #4
    global inicio
    inicio = None #puxo a variável 'inicio' e atribuo a ela o 'vazio'. Poderia verificar aqui tbm antes de limpar, se o histórico de sites está vazio ou não
    print(" Histórico completamente limpo!")

def buscar_site(): #opção #5
    if inicio is None:
        print(" Histórico está vazio!")
        return

    url = input(" Digite o endereço do site a buscar: ").strip() #remove espaços em branco - pré processamento
    
    atual = inicio
    while atual is not None: #verifica se ja foi cessado algum site
        if atual["url"] == url: #verifica a existencia do site informado no histórico
            print(f" Site encontrado: {atual['url']} às {atual['horario']}")
            return
        atual = atual["prox"] #verifica se o mesmo site foi acessado mais de uma vez

    print(f" Site '{url}' não encontrado.")


while True:
    print("\n========== Menu de Histórico de Navegação ==========")
    print(" [1] - Acessar novo site")
    print(" [2] - Ver histórico completo")
    print(" [3] - Remover site do histórico")
    print(" [4] - Limpar todo o histórico")
    print(" [5] - Buscar site pelo endereço")
    print(" [6] - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == '1':
        acessar_site()
    elif opcao == '2':
        mostrar_historico()
    elif opcao == '3':
        remover_site()
    elif opcao == '4':
        confirmar = input("Tem certeza que deseja limpar tudo? (s/n): ").lower() #mesmo se o user informa em maiúsculo, ele converte para fazer a leitura
        if confirmar == 's':
            limpar_historico()
    elif opcao == '5':
        buscar_site()
    elif opcao == '6':
        print("Saindo do sistema...")
        time.sleep(1)
        break
    else:
        print(" Opção inválida! Tente novamente.")

    time.sleep(0.5)