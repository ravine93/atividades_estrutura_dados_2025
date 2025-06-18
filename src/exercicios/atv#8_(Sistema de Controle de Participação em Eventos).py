"""
Módulo para atividade #8 de Estrutura de Dados.
Sistema de controle de participação em eventos usando sets. Gerencia participantes de 
eventos técnicos/culturais com operações de conjuntos. Menu interativo para cadastro, 
consulta e remoção de participantes, exibindo interseções e diferenças entre eventos.
"""
import time

evento_tecnico = set() #conjuntos
evento_cultural = set() # conjuntos

def inserir_participantes(evento):
    qtd = int(input(" Quantos nomes deseja inserir? "))
    for i in range(qtd):
        nome = input(" Digite o nome do participante: ").strip() #processamento do input
        evento.add(nome)
    print(" Participantes adicionados com sucesso!")

def remover_participante():
    print("\n De qual evento deseja remover?")
    print(" 1 - Evento Técnico")
    print(" 2 - Evento Cultural")
    opcao = input(" Escolha: ")
    
    nome = input(" Digite o nome do participante a remover: ").strip()
    
    if opcao == '1':
        if nome in evento_tecnico:
            evento_tecnico.remove(nome)
            print(f"{ nome} removido do Evento Técnico!")
        else:
            print(" Participante não encontrado no Evento Técnico!")
    elif opcao == '2':
        if nome in evento_cultural:
            evento_cultural.remove(nome)
            print(f" {nome} removido do Evento Cultural!")
        else:
            print(" Participante não encontrado no Evento Cultural!")
    else:
        print(" Opção inválida!")

def mostrar_intersecao():
    comuns = evento_tecnico & evento_cultural
    print("\n Participantes dos DOIS eventos:")
    if comuns:
        print(comuns)
    else:
        print(" Nenhum participante em comum em ambos os eventos")

def mostrar_apenas_um():
    unicos = evento_tecnico ^ evento_cultural
    print("\n Participantes de APENAS UM evento:")
    if unicos:
        print(unicos)
    else:
        print(" Nenhum participante participou de apenas um dos eventos")

def consultar_participante():
    nome = input("Digite o nome do funcionário: ").strip() #processamento do input
    no_tecnico = nome in evento_tecnico
    no_cultural = nome in evento_cultural
    
    if no_tecnico and no_cultural:
        print(f" {nome} participou dos DOIS eventos")
    elif no_tecnico:
        print(f" {nome} participou apenas do Evento Técnico")
    elif no_cultural:
        print(f" {nome} participou apenas do Evento Cultural")
    else:
        print(f" {nome} não participou de nenhum evento")

# Menu principal
while True:
    print("\n === Menu de Consulta de Participação ===")
    print(" 1 - Inserir participantes do Evento Técnico")
    print(" 2 - Inserir participantes do Evento Cultural")
    print(" 3 - Remover participante de um evento")
    print(" 4 - Mostrar funcionários que participaram dos DOIS eventos")
    print(" 5 - Mostrar funcionários que participaram de APENAS UM evento")
    print(" 6 - Consultar se um funcionário participou (e de quais eventos)")
    print(" 7 - Sair")
    
    opcao = input(" Escolha uma opção: ")
    
    if opcao == '1':
        inserir_participantes(evento_tecnico)
    
    elif opcao == '2':
        inserir_participantes(evento_cultural)
    
    elif opcao == '3':
        remover_participante()
    
    elif opcao == '4':
        mostrar_intersecao()
    
    elif opcao == '5':
        mostrar_apenas_um()
    
    elif opcao == '6':
        consultar_participante()
    
    elif opcao == '7':
        print(" Encerrando o sistema...")
        time.sleep(1)
        break
    
    else:
        print("Opção inválida! Tente novamente.")
    
    time.sleep(0.5)