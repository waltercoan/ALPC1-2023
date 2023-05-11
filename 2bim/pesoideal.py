'''
5)	Faça um programa que receba a altura e o sexo 
de uma pessoa e que calcule e mostre o seu peso 
ideal, utilizando as seguintes formulas:
a.	Para homens: (72.7 * h) – 58
b.	Para mulheres: (62.1 * h) – 44.7
'''
print("Digite a altura")
altura = float(input())
print("Digite o sexo M/F")
sexo = input()
peso = 0
if sexo == 'm' or sexo == 'M':
    peso = (72.7 * altura) - 58
    #aqui1
else:
    if sexo == 'f' or sexo == 'F':
        peso = (62.1 * altura) - 44.7
    else:
        print("Sexo invalido")
print("O peso ideal e ", peso)