'''
REPETIÇÃO6) Elaborar um programa que 
efetue a leitura de 10 valores numéricos
e apresente no final o total do somatório
e a média do total.
'''
cont = 0
soma = 0
while cont < 10:
    print("Digite um numero")
    num = int(input())
    #acumulador
    soma = soma + num
    #contador
    cont +=1
print("A soma e ", soma)
media = soma / 10
print("A media e ", media)

