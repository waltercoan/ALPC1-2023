'''
Elaborar um programa que efetue a leitura
de valores positivos inteiros até que 
um valor negativo seja informado. 
Ao final deve ser apresentados 
o maior e o menor número 
informado pelo usuário.
'''
omaiornum = 0
omenornum = 0
conta = 0
while True:
    print("Digite um numero")
    num = int(input())
    if num < 0:
        break
    if num > omaiornum:
        omaiornum = num
    #NUMCA MISTURAR A LOGICA DO MAIOR COM O MENOR
    if conta == 0:
        omenornum = num
    else:
        if num < omenornum:
            omenornum = num
    conta += 1

print("O maior numero e", omaiornum)
print("O menor numero e", omenornum)