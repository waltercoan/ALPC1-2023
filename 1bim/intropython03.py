#ENTRADAS
print("Digite a distancia em KM")
distancia = int(input())
#PROCESSAMENTO
litros = distancia / 13
valreemb = 2.2 * litros
#SAIDA - String interpolation
print(f"O valor do reemb e {valreemb:.2f}%")
