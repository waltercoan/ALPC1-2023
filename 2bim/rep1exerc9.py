'''
Faça um programa que receba vários números, calcule e mostre:
- a soma dos números digitados;
- a quantidade de números digitados;
- a média dos números digitados; 
- o maior número digitado;
- o menor número digitado;
- a média dos números pares;
- a porcentagem dos números ímpares entre todos os 
números digitados.
Finalize a entrada de dados com a digitação do número 30000.
'''
soma = 0
contador = 0
omaior = 0
omenor = 0
somapares = 0
contapares = 0
while True:
    print("Digite um numero")
    numero = int(input())
    if numero == 30000:
        break
    if numero % 2 == 0:
        #numero par
        contapares += 1 #contapares = contapares + 1
        somapares += numero
        #somapares = somapares + numero
    
    soma = soma + numero #acumulador
    contador = contador + 1 #contador
    if numero > omaior:
        omaior = numero
    #nunca misturar a logica do maior com a do menor
    if contador == 1:
        omenor = numero
    else:
        if numero < omenor:
            omenor = numero

print("A soma e ", soma)
print("A qtd e ", contador)
media = soma / contador
print("A media e ", media)
print("O maior numero e ", omaior)
print("O menor numero e ", omenor)
if contapares > 0:
    mediapares = somapares / contapares
    print("Media dos pares ", mediapares)
contaimpar = contador - contapares
# contador ----- 100%
# contaimpar --- percimpar
percimpar = (contaimpar * 100) / contador
print("O perc de impares e", percimpar)