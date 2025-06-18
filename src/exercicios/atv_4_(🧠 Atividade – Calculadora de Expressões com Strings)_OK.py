"""Módulo para atividade #4 de Estrutura de Dados.
Calculadora de expressões em strings: processa operações como "a+b" ou 
múltiplas "x+y, w-z", converte e calcula, tratando erros (divisão por zero, sintaxe inválida).
"""

lista_expressoes = []

entrada_bruta_exp = input("\n Informe as expressões a serem calculadas (separe-as por vírgula): ")
print("")

#leia-se: 'para cada expressao, dentro do input, faça'
#.split: cada vez que aparecer a vírgula, é identificado uma nova expressão
for expressao in entrada_bruta_exp.split(','):
    #remover os espaços vazios nas expressões identificadas e as armazena na variável
    expressao_limpa = expressao.replace(" ", "")
    #adicionar à lista as expressões depois de padronizadas
    lista_expressoes.append(expressao_limpa)
    if len(expressao_limpa) < 3:
        print(f" ERRO: [{expressao_limpa}=] está incompleta!\n")
        continue

    #variável de inicialização: =! de 0 por ser uma string.
    #aqui é armazenado o operador que for identificado
    #pylint: disable=invalid-name
    operador_valido = None
    #contabilizar quantos operadores tem
    qtt_operador = 0
    #o valor negativo é para indicar que não há operador identificado.
    #quando houver, o valor será o índice do operador
    posic_operador = -1
    indice_operador = 0
    operadores_validos = ['+', '-', '*', '/']


    for caract in expressao_limpa:
        if caract in operadores_validos:
            operador_valido = caract
            #garantir que haja apenas 1 operador por expressão
            qtt_operador = qtt_operador + 1
            #valor utilizado para separar os numeros com base no índice do operador
            posic_operador = indice_operador
            #saber índice do operador pela ação do 'for' de cada 'expressao_limpa'
            #dentro da 'lista_expressoes'
        indice_operador = indice_operador + 1
        
    if qtt_operador < 1:
        print(f" ERRO: [{expressao_limpa}=] não possui de operador!\n")
        continue
    elif qtt_operador > 1:
        print(f" ERRO: [{expressao_limpa}=] possui mais de um operador!\n")
        continue

    #armazena todos os caracteres que existam antes do operador
    num1_str = expressao_limpa[:posic_operador]
    #armazena todos os caracteres que existam após um índice de onde está o operador
    num2_str = expressao_limpa[posic_operador+1:]
    digito_valido = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num1_valido = True
    num2_valido = True
    
    #necessário por ainda não ter convertido a entrada de str para int
    #aqui eu tiro a possibilidade de considerar "." e "-"
    for dig_1 in num1_str:
        if dig_1 not in digito_valido:
            num1_valido = False
            break

    for dig_2 in num2_str:
        if dig_2 not in digito_valido:
            num2_valido = False
            break

    if not num1_valido:
        print(f" ERRO: [{expressao_limpa}=] contém o primeiro valor inválido --> {num1_str}\n")
        continue

    if not num2_valido:
        print(f" ERRO: [{expressao_limpa}=] contém o segundo valor inválido --> {num2_str}\n")
        continue

    num1_int = int(num1_str)
    num2_int = int(num2_str)

    if operador_valido == '/' and num2_int == 0:
        print(f" ERRO: há uma divisão por zero em [{expressao_limpa}=]!\n")
        continue

    if operador_valido == '+':
        resultado = num1_int + num2_int
    elif operador_valido == '-':
        resultado = num1_int - num2_int
    elif operador_valido == '*':
        resultado = num1_int * num2_int
    elif operador_valido == '/':
        resultado = num1_int / num2_int
    
    resultado = int(resultado)
    if resultado < 0:
        print(f" ERRO: [{expressao_limpa}=] dá um resultado negativo! --> {resultado}\n")
    else:    
        print(f" [{expressao_limpa}=] --> {num1_int} {operador_valido} {num2_int} = {resultado}\n")
