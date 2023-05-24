'''
conta = 0
soma = 0
while conta <= 500:
    print(conta, end=" ")
    soma = soma + conta #acumulador
    conta = conta + 2 #contador

print("\nA soma e", soma)
'''
conta = 0
soma = 0
while conta <= 500:
    #se conta resto da divisao por 2 igual zero entao
    if conta % 2 == 0:
        print(conta, end=" ")
        soma = soma + conta #acumulador
    conta = conta + 1 #contador

print("\nA soma e", soma)