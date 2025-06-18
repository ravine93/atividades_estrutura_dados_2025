"""Módulo para atividade #1 de Estrutura de Dados.
Recebe nome e 4 notas do aluno, calcula a média e retorna 
se está aprovado (>=6), reprovado (<5) ou em recuperação.
"""

nm_aluno = input(" Informe o nome do aluno(a): ")
nt_1 = float(input(" Informe a nota 1/4: "))
nt_2 = float(input(" Informe a nota 2/4: "))
nt_3 = float(input(" Informe a nota 3/4: "))
nt_4 = float(input(" Informe a nota 4/4: "))

media_final = (nt_1+nt_2+nt_3+nt_4)/4

if media_final < 5.0:
    print(f"\n Média final {media_final}")
    print(" Aluno(a) reprovado(a!")
elif media_final >= 6.0:
    print(f"\n Média final {media_final}")
    print(" Aluno(a) Aprovado(a)!")
else:
    print(f"\n Média final {media_final}")
    print(" Aluno(a) em recuperação!")
