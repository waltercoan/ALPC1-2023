'''
REPETIÇÃO3) Faça um programa que leia um 
valor N inteiro e positivo. Calcule e 
mostre o valor de E, conforme a fórmula a seguir:
E = 1 + 1/(1!) + 1/(2!) 
+ 1/(3!) + ... + 1/(N!)
'''
print("Digite o valor do N")
n = int(input())
cont = 1
E = 1
while cont <= n:
    print(cont,"!=",end="")
    fat = cont
    resultado = 1
    while fat >= 1:
        #print(fat, end=" ")
        resultado = resultado * fat
        fat = fat - 1
    print(resultado)
    E = E + (1/resultado)
    cont += 1
print("E = ", E)