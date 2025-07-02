"""Módulo para atividade #12 de Estrutura de Dados.
Simula sistema de arquivos com pastas e arquivos usando
dicionários aninhados e funções recursivas para navegação.
--> continuação do exercício anterior"""

def criar_pasta(nome): #nó para a pasta --> permite inserção apenas de valores para a chave 'nome' 
    return {
        "nome": nome,
        "tipo": "pasta",
        "filhos": [] #aqui ficarão outras pastas, a chave 'tipo' seja = 'pasta'
    }

def criar_arquivo(nome, tamanho): #nó para o arquivo --> permite inserção apenas das chaves 'nome' e 'tamanho'
    return {
        "nome": nome,
        "tipo": "arquivo",
        "tamanho": tamanho
    } #sem 'filhos' por serem os arquivos e não pastas de armazenagem dos mesmos

def adicionar_item(pasta_destino, item):
    if pasta_destino["tipo"] == "pasta": #se não for um 'arquivo', uma nova pasta será criada dentro da pasta local e associada a chave 'filhos'
        pasta_destino["filhos"].append(item)
    else:
        print(f"ERRO: Não é possível adicionar item em '{pasta_destino['nome']}', pois não é uma pasta.")

def imprimir_estrutura(pasta, prefixo=""): #impressão do nó
    if pasta["tipo"] == "pasta":
        print(f"{prefixo}└── {pasta['nome']}/") #impressão do caractere especial seguido da pasta + '/'
        filhos = pasta["filhos"]
        for i, filho in enumerate(filhos):
            if i == len(filhos) -1: #pegar o último elemento da lista
                novo_prefixo = prefixo + "    " #caso seja o último elemento da lista, um tab será inserido
            else: #se não for o último elemento da lista, a linha se iniciará com a barra vertical abaixo
                novo_prefixo = prefixo + "│   "
            imprimir_estrutura(filho, novo_prefixo)
    else:
        # Arquivo
        print(f"{prefixo}└── {pasta['nome']} ({pasta['tamanho']} KB)")

def calcular_tamanho(pasta): #função recursiva que sooma tamanho relacionado a pasta e em seguida os arquivos dentro dela. caso haja outra pasta dentro desta primera pasta, ele vai repetindo o processo e incrementando os valores até chegar num lugar em que não hajam mais pastas
    if pasta["tipo"] == "arquivo":
        return pasta["tamanho"] 
    else:
        total = 0
        for filho in pasta["filhos"]:
            total += calcular_tamanho(filho) #soma o tamanho da pasta anterior com o tamanho de todos os arquivos desta pasta em questão
        return total


#exemplo de uso:
raiz = criar_pasta("root")

docs = criar_pasta("documentos")
img = criar_arquivo("foto.png", 150)
txt = criar_arquivo("texto.txt", 50)
pdf = criar_arquivo("texto.txt", 80)
jpeg = criar_arquivo("texto.txt", 76)

adicionar_item(docs, txt)
adicionar_item(raiz, docs)
adicionar_item(raiz, img)
adicionar_item(raiz, pdf)
adicionar_item(raiz, jpeg)

imprimir_estrutura(raiz)
print(" \nTamanho total da pasta 'root':", calcular_tamanho(raiz), "KB")