'''
REPETIÇÃO7) Elaborar um programa que 
efetue a leitura sucessiva de valores 
numéricos e apresente no final o total 
do somatório, a média e o total de valores
lidos. O programa deve fazer as leituras 
dos valores enquanto o usuário estiver 
fornecedor valores positivos. Ou seja, 
o programa deve parar quando o usuário 
fornecer um valor negativo.
'''
soma = 0
contador = 0
while True:
    print("Digite o numero")
    num = int(input())
    if num < 0:
        break
    soma += num
    contador += 1
print("Somatorio",  soma)
media = soma / contador
print("Media", media)
print("Qtd Numeros ", contador)