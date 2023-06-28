'''
REPENQ6) Faça um programa que receba o valor do salário 
mínimo e uma lista contendo a quantidade de quilowatts 
gasta por consumidor e o tipo do consumidor (1-Residencial, 
2-Comercial, 3-Industrial).
Calcule e mostre:
- O valor de cada quilowatt, sabendo que o quilowatt 
custa 1/8 do salário mínimo;
- O valor a ser pago por cada consumidor (conta final 
mais acréscimos), considerando que o acréscimo é o mesmo 
da tabela a seguir:
Tipo	% de acréscimo sobre o valor gasto
1	    5
2	    10
3	    15

- O faturamento geral da empresa
- a quantidade de consumidores que pagam 
entre R$ 500,00 e R$ 1000,00
Termine a entrada de dados quando a quantidade de 
quilowatts digitada for igual a zero.
'''

print("Digite o salario minimo")
salmin = float(input())

valkw = salmin / 8
print("O valor do quilowats hora e", valkw)

total = 0
contador = 0
while True:
    print("Digite a qtd de quilowats consumida")
    qtd = float(input())
    if qtd == 0:
        break
    print("Digite o tipo: 1 Res - 2 Comer - 3 Indus")
    tipo = int(input())

    valbase = valkw * qtd
    perc = 0
    if tipo == 1:
        perc = 5
    else:
        if tipo == 2:
            perc = 10
        else: 
            perc = 15
    valbase = valbase + (valbase * perc /100)
    print("O valor da conta e ", valbase)
    if valbase >= 500 and valbase <= 1000:
        contador = contador + 1
    total += valbase

print("O faturamento da empresa ", total)
print("O numero de clientes com conta entre 500 e 1000 e ",contador)
