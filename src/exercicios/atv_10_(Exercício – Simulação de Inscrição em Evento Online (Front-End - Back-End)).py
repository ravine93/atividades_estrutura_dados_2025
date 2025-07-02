"""Módulo para atividade #10 de Estrutura de Dados.
Simula inscrição em evento online com validações de dados
entre front-end e back-end usando JSON e lista de registros."""


import json
import time

banco_de_dados = [] #lista para armazenar o dicionário dos dados dos inscritos

def menu_frontend(): #front-end
    while True:
        print("\n Formulário de Inscrição no Evento")
        nome = input(" Nome: ")
        email = input(" Email: ")
        idade = int(input(" Idade: "))
        interesse = input(" Interesse (Programação / Design / Marketing): ")

        dados_usuario = {
            "nome": nome,
            "email": email,
            "idade": idade,
            "interesse": interesse
        }

        json_enviado = json.dumps(dados_usuario) #serialização com json.dumps() + envio p back-end
        print("\n Enviando dados para o servidor...")
        time.sleep(1)
        resposta = processar_inscricao(json_enviado)  #resposta do "servidor" --> chamada da função onde os dados são transformados de dicionṕarios em listas para arquivos JSON

        print("\n Resposta do servidor:") #respostas do servidor conforme situação
        print(f" Status: {resposta['status']}")
        print(f" Mensagem: {resposta['mensagem']}")

        opcao = input(" \nDeseja fazer outra inscrição? (s/n): ").strip().lower() #remover espaços e padronizar a resposta em minúsculo antes da verificação
        if opcao != 's': #caso não seja 's' ele pára o loop aqui e mostra tudo o que ja foi cadastrado com sucesso
            break

    print("\n Lista de inscritos válidos:")
    for i, inscrito in enumerate(banco_de_dados, 1): #i (posição vetorial) está relacionado ao 'banco_de_dados' e 1 está relacionado a variáve 'inscrito'
        print(f"{i}. {inscrito['nome']} - {inscrito['email']} - {inscrito['interesse']}")



def processar_inscricao(json_recebido): #back-end
    dados = json.loads(json_recebido)  # desserializa --> pega o JSON recebido e o transforma em uma lista 

    nome = dados.get("nome", "").strip() #uso o get aqui para que ele pegue apenas o valor relacionado à chave 'nome'. caso não haja nada relacionado à chave, um valor vazio é inserido '""' como padrão
    email = dados.get("email", "").strip()
    idade = dados.get("idade", 0) #caso a não tenham informado a idade, o numero 0 é associado a chave 'idade'. consequentemente o incrito será invalidado por ser menor do que 16 anos
    interesse = dados.get("interesse", "").strip()

	#regras de negócio
    if len(nome) < 3: 
        return {"status": "ERRO", "mensagem": "Erro: nome deve ter ao menos 3 letras."}
    if "@" not in email or not email.endswith(".com"): #auto explicativo
        return {"status": "ERRO", "mensagem": "Erro: email inválido."}
    if idade:
        try:
            idade_int = int(idade) #conversão da str, caso for numérica, para inteiro
        except:
            return {"status": "ERRO", "mensagem": "Erro: idade inválida."} 
        if idade_int < 16:
            return {"status": "ERRO", "mensagem": "Erro: idade mínima não atingida ou idade inválida."}    
    else:
        return {"status": "ERRO", "mensagem": "Erro: idade não informada."}
    if interesse not in ["Programação", "Design", "Marketing"]: #como não fiz pre processamento, o sistema só vai aceitar se estiver escrito exatamente como na verificação
        return {"status": "ERRO", "mensagem": "Erro: interesse inválido."}

    banco_de_dados.append(dados) #adiciono à lista global os dados extraídos do JSON

    return { #garantir que seja retornado apenas dados que não passaram pelos 4 if's anteriores
        "status": "Sucesso",
        "mensagem": "Inscrição realizada com sucesso!"
    }


# Execução principal
menu_frontend()