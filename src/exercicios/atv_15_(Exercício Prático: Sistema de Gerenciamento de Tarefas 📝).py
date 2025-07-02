# obter_valor_dicionario.py
# Módulo para obter valores de um dicionário através de uma chave

def executar():    
    dicionario_produtos = {
        'produto': 'Notebook',
        'preco': 4500
    }
    
    print(" Consulta de Dicionário ")
    print(f" --> Dicionário disponível: {dicionario_produtos}")
    print(f" --> Chaves disponíveis: {list(dicionario_produtos.keys())}")
    print()
    
    chave_busca = input(" Chave a ser consultada: ")
    
    if chave_busca in dicionario_produtos:
        valor = dicionario_produtos[chave_busca]
        print(f"O valor da chave '{chave_busca}' é '{valor}'.")
    else:
        print(f"Erro: A chave '{chave_busca}' não foi encontrada no dicionário.")

if __name__ == "__main__":
    executar()