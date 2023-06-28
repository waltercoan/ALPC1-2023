'''
REPENQ2) Faça um algoritmo que leia um 
número inteiro e calcule o seu fatorial. 
Se o número for negativo, informe que o valor 
é inválido. Sabemos que o fatorial de um número 
n, representado por n!, é dado por:
n * (n-1) * (n-2) * ... * 1, para n > 0 e 
n! = 1 para n = 0
'''

print("Digite um numero")
fat = int(input())
if fat < 0:
    print("Valor invalido")
else:
    cont = fat
    result = 1
    # 5! = 5 * 4 * 3 * 2 * 1
    while cont > 0:
        print(cont, end=' * ')
        result = result * cont
        cont = cont - 1
        #aqui1
    print("\n",fat,"!=",result)
#aqui3