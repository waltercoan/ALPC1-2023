'''
Faça um programa que apresente os resultados 
de uma tabuada de um número qualquer, a 
qual deve ser impressa no seguinte formato:
Considerando como exemplo o fornecimento do 
número 2 para o número qualquer, 
ter-se-ia a seguinte situação:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
2 x 10 = 20
'''

print("Digite o numero da tabuada")
tabuada = int(input())

for i in range(1,11):
    result = tabuada * i
    #String Interpolation
    print(f"{tabuada} X {i} = {result}") 
    #print(tabuada," X ", i , " = ", result)
