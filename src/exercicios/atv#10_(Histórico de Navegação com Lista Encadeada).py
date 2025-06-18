"""Módulo para atividade #10 de Estrutura de Dados.
Capaz de cadastrar, listar, alterar e excluir dados de
dicionários contidos em uma lista
"""


import json

#FRONT-END
formulario = {}

dados = {
	'nome' : 'in_nome',
	'email' : 'in_email',
	'idade' : 'in_idade',
	'interesse' : 'in_interesse'
}

in_nome = input(" Informe o nome do inscrito: "),
in_email = input("Informe o e-mail: "),
in_idade = int(input("Informe a idade: ")),
in_interesse = input("Informe o assunto de interesse: ")

formulario[dados] = [{in_nome, in_email, in_idade, in_interesse}]

# Converte para JSON para simular envio ao back-end
dados_json = json.dumps(formulario)

resposta_json = simular_back_end(dados_json)

	# Converte resposta de volta para dicionário
	resposta = json.loads(resposta_json)

	print("\n[FRONT-END] Resposta do servidor:")
	print(resposta)

json_forms = json.dumps(dados)
print(type(json_forms))
print("Dados (FRONT-END):", json_forms)

#BACK-END
while True:
	if len(nome) < 3:
    	print("\n ...status: erro\n")
    	print(" Erro: nome com com menos de 3 caracteres")
    	break
   	 
	if '@' not in email:
    	print("\n ...status: erro\n")
    	print(" Erro: '@' ausente no endereço de e-mail")
    	break
	if '.com' not in email:
    	print("\n ...status: erro\n")
    	print(" Erro: '.com' ausente no endereço de e-mail")
    	break
    
	if idade < 16:
    	print("\n ...status: erro\n")
    	print(" ERRO: Idade inferior ao permitido. Idade mínima: 16 anos")
    	break
    
	if interesse =! 'Programação' and interesse =! 'Design' and interesse =! 'Marketing':
    	print("\n ...status: erro\n")
    	print(" Erro: área de interesse indisponível")
    	print(" Áreas disponíveis:\n Programação\n Design\n Marketing")
    	break
    
	print("\n ...status: sucesso\n")
	print(" Inscrição realizada com sucesso!")
    
    

   	 
    


# JSON (string) → Dicionário
dicionario = json.loads(json_str)
print(type(dicionario))
print(dicionario)  # {'nome': 'João', 'idade': 30}
print(dicionario["nome"])  # João'''




    





