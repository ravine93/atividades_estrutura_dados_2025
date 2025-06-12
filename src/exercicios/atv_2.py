"""Módulo para atividade #2 de Estrutura de Dados.
Capaz de verificar e liberar acessos prediais
"""

while True:
    in_out = input(" Deseja entrar no prédio? (entrar/sair): ")
    if in_out == 'entrar':    
        nome = input(" Olá, por favor, informe seu nome: ")
        horario = int(input(" Informe o horário de entrada: "))
        if horario >= 0 and horario <= 23:
            cat_acesso = input(" Qual é sua categoria de acesso:\n   A --> Morador(a)\n   B --> Visitante\n   C --> Prestador(a) de Serviços\n")
            if cat_acesso == 'A':
                print(f" Certo morador(a) {nome}, acesso liberado!")
            elif cat_acesso == 'B' and (horario >= 8 and horario <= 22):
                print(f" Certo {nome}, você é um visitante, e está dentro do horário de visita. \n Acesso liberado!")
            elif cat_acesso == 'B' and (horario < 8 or horario > 22):
                print(f" Certo {nome}, você é um visitante, e está fora do horário de visita. \n Acesso negado!")
            elif cat_acesso == 'C' and (horario >= 8 and horario <= 18):
                print(f" Certo {nome}, você veio à trabalho, acesso liberado!")
            elif cat_acesso == 'C' and (horario < 8 or horario > 18):
                print(f" Certo {nome}, você veio à trabalho, mas está fora do horário. Acesso negado!")
            else:
                print(" Opção informada inválida! Tente novamente")
        else:
            print(" Horário inválido! Informe um valor de 0 à 23")
    elif in_out == 'sair':
        print(" Saindo...")
        break
    else:
        print(" Tente novamente, opção inválida!")
        