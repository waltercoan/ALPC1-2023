#entradas
print("Digite um numero")
num1 = int(input())
print("Digite outro numero")
num2 = int(input())

if num1 == num2:
    #bloco do sim
    print("Sao iguais")
    media = (num1 + num2)/2
    print("A media e", media)
else:
    #BLOCO DO NAO
    if num1 > num2:
        print("Maior", num1, "menor",num2)
    else:
        print("Maior", num2, "menor",num1)