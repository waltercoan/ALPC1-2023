'''
REPENQ3) Faça um algoritmo que calcule a soma de 
todos os números ímpares dentro de uma faixa de 
valores determinada pelo usuário. Um número é 
ímpar quando sua divisão por 2 não é exata, 
ou seja, o resto resultante da divisão inteira
pelo número 2 tem valor 1. Utilize a 
palavra resto como operador que calcula o 
resto da divisão de um numero por outro.
'''
print("Digite o numero inicial")
ini = int(input())
print("Digite o numero final")
fim = int(input())

soma = 0
for i in range(ini,fim+1):
    print(i, end=" ")
    # se i RESTO_DA_DIV por 2 for igual a um
    if i % 2 == 1: 
        #numero impar
        soma = soma + i
print("A soma dos impares e ", soma)

#for i in range(10): ZERO ATE NOVE
#for i in range(0,10): ZERO ATE NOVE
#for i in range(0,10,2): ZERO, DOIS, QUATRO, SEIS, OITO