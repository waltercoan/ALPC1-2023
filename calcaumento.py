print("Digite o preco do produto")
preco = float(input())

perc=0
if preco <= 50:
    perc=5
else: 
    if preco > 50 and preco <= 100:
        perc=10
    else:
        perc=15
valaumento = (preco * perc) / 100
novopreco = preco + valaumento
print("O novo preco e", novopreco)

if novopreco <= 80:
    print("Barato")
else:
    if novopreco > 80 and novopreco <= 120:
        print("Normal")
    else:
        if novopreco > 120 and novopreco <= 200:
            print("Caro")
        else:
            print("Muito caro")