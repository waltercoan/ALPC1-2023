print("Digite o valor de venda media mensal")
valmedia = float(input())
print("Digite o preco atual")
precoatual = float(input())

novopreco = 0
if valmedia < 500 or precoatual < 30:
    novopreco = precoatual + (precoatual * 12 / 100)
else:
    if (valmedia >= 500 and valmedia < 1600) or \
        (precoatual >= 30 and precoatual < 80):
        novopreco = precoatual + (precoatual * 15 / 100)
    else:
        novopreco = precoatual - (precoatual * 25 / 100)
print("O novo preco e", novopreco)