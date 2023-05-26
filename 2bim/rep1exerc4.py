'''
Faça um programa que leia um número N 
que indica quantos valores inteiros e positivos
devem ser lidos a seguir. Para cada número lido, 
mostre o valor lido e o fatorial desse valor.
'''

#Faça um programa que leia um número N 
print("Digite um numero")
n = int(input())
conta = 0
while conta < n:
    print("Digite o numero do fatorial")
    fat = int(input())
    outroconta = 1
    resultado = 1
    while outroconta <= fat:
        #print(outroconta)
        resultado = resultado * outroconta
        outroconta = outroconta + 1
    print(fat,"!=", resultado)
    conta = conta + 1
