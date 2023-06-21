'''
Faça um algoritmo que calcule a média de
todas as turmas de uma escola. Considere 
como entradas o número de turmas e o 
número de alunos de cada turma. A 
média de cada turma deve ser apresentada, 
além da média geral, que será o 
resultado da média das turmas.
'''
print("Digite o numero de turmas")
turmas = int(input())

somamedias = 0
for contaturma in range(turmas):
    print("Turma", contaturma+1)
    print("Digite o num de alunos")
    alunos = int(input())
    soma = 0
    for contaaluno in range(alunos):
        print("Aluno", contaaluno+1)
        print("Digite a nota")
        nota = float(input())
        soma = soma + nota
    media = soma / alunos
    print("A media e", media)
    somamedias = somamedias + media
mediaescola = somamedias / turmas
print("A media da escola e", mediaescola)