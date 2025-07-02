"""
Módulo para atividade #8 de Estrutura de Dados.
Sistema de controle de participação em eventos usando sets. Gerencia participantes de 
eventos técnicos/culturais com operações de conjuntos. Menu interativo para cadastro, 
consulta e remoção de participantes, exibindo interseções e diferenças entre eventos.
"""
import time

evento_tecnico = set() #conjunto vazio --> garantir que não hajam nomes repetidos
evento_cultural = set() # conjunto vazio

def inserir_participantes(evento): #função p opção #1 e #2 (alocação especificada por evento ocorre na chamada da função)
    qtd = int(input(" Quantos nomes deseja inserir? "))
    for i in range(qtd): #pega o valor inserido e usa como limite para o loop
        nome = input(" Digite o nome do participante: ").strip() #processamento do input
        evento.add(nome) #adiciona o nome informado ao conjunto "evento" através do parâmetro "nome" via método "add"
    print(" Participantes adicionados com sucesso!")

def remover_participante(): #função p opção #3
    print("\n De qual evento deseja remover?") #submenu para garantir que a remoção parta de um evento específico
    print(" 1 - Evento Técnico")
    print(" 2 - Evento Cultural")
    opcao = input(" Escolha: ")
    
    nome = input(" Digite o nome do participante a remover: ").strip()
    
    if opcao == '1':
        if nome in evento_tecnico:
            evento_tecnico.remove(nome)
            print(f" {nome} removido do Evento Técnico!")
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

def mostrar_intersecao(): #função p opção #4
    comuns = evento_tecnico & evento_cultural #'&' caractere que indica uma intersecção. ou seja, considera apenas os elementos presentes em ambos os conjuntos
    print("\n Participantes dos DOIS eventos:")
    if comuns:
        print(comuns)
    else:
        print(" Nenhum participante em comum em ambos os eventos")

def mostrar_apenas_um(): #função p opção #5
    unicos = evento_tecnico ^ evento_cultural #'^' caractere que indica uma diferença. ou seja, considera apenas os elementos presentes em um dos conjuntos
    print("\n Participantes de APENAS UM evento:")
    if unicos:
        print(unicos)
    else:
        print(" Nenhum participante participou de apenas um dos eventos")

def consultar_participante(): #função p opção #6
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


while True: #menu principal
    print("\n ======== Menu de Consulta de Participação ========")
    print(" 1 - Inserir participantes do Evento Técnico")
    print(" 2 - Inserir participantes do Evento Cultural")
    print(" 3 - Remover participante de um evento")
    print(" 4 - Mostrar funcionários que participaram dos DOIS eventos")
    print(" 5 - Mostrar funcionários que participaram de APENAS UM evento")
    print(" 6 - Consultar se um funcionário participou (e de quais eventos)")
    print(" 7 - Sair")
    
    opcao = input(" Escolha uma opção: ")
    
    if opcao == '1':
        print(" Inserir participante ao Evento Técnico: ")
        inserir_participantes(evento_tecnico)
    
    elif opcao == '2':
        print(" Inserir participante ao Evento Cultural: ")
        inserir_participantes(evento_cultural)
    
    elif opcao == '3':
        print(" Remover participante: ")
        remover_participante()
    
    elif opcao == '4':
        print(" Funcionários participantes de ambos os Eventos: ")
        mostrar_intersecao()
    
    elif opcao == '5':
        print(" Funcionários participantes de apenas um dos Eventos: ")
        mostrar_apenas_um()
    
    elif opcao == '6':
        print(" Listando funcionário específico: ")
        consultar_participante()
    
    elif opcao == '7':
        print(" Encerrando o sistema...")
        time.sleep(1)
        break
    
    else:
        print("Opção inválida! Tente novamente.")
    
    time.sleep(0.5)