print("Digite o primeiro numero")
numA = int(input())
print("Digite o segundo numero")
numB = int(input())
print("Digite o terceiro numero")
numC = int(input())

if numA > numB:
    #bloco do SIM
    if numA > numC:
        #Bloco do SIM
        print("O maior e", numA)
        if numB > numC:
            #bloco do SIM
            print("O do meio e", numB)
            print("O menor e", numC)
        else:
            #Bloco do NAO
            print("O do meio e", numC)
            print("O menor e", numB)
    else:
        #Bloco do não
        print("O maior e", numC)
        print("O do meio e", numA)
        print("O menor e", numB)
else:
    #Bloco do NÃO
    if numB > numC:
        #bloco do SIM
        print("O maior e", numB)
        if numA > numC:
            print("O do meio", numA)
            print("O menor e", numC)
        else:
            print("O do meio", numC)
            print("O menor e", numA)
    else:
        #Bloco do não
        print("O maior e", numC)
        print("O do meio", numB)
        print("O menor e", numA)