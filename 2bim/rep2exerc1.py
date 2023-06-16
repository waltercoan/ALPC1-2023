'''
Faça um algoritmo que calcule a 
multiplicação de dois números inteiros
sem utilizar o operador “*”. Em 
vez disso, utilize apenas o operador 
de adição “+”. Para implementar esse
algoritmo, devemos lembrar que qualquer
multiplicação pode ser expressa por 
meio de somas. Por exemplo, o resultado 
da expressão 6 * 3 é o mesmo q
ue 6 + 6 + 6 ou 3 + 3 + 3 + 3 + 3 + 3. 
Ou seja, soma-se um elemento com ele 
próprio o número de vezes do segundo elemento.
'''

print("Digite o primeiro numero")
num1 = int(input())

print("Digite o segundo numero")
num2 = int(input())

soma = 0

for i in range(num2):
    soma = soma + num1
#cont = 0
#while cont < num2:
#    soma = soma + num1
#    cont +=1 

print("Resultado = ", soma)