'''
3)	Efetuar o cálculo e a apresentação do 
valor de uma prestação em atraso, utilizando a 
fórmula: 
PRESTACAO = VALOR + (VALOR *(TAXA/100) * TEMPOEMDIAS).
'''
print("Digite o valor da prestacao em atraso")
valor = float(input())
print("Digite o percentual da multa")
taxa = float(input())
print("Digite o numero de dias")
tempoemdias = int(input())
prestacao = valor + (valor * (taxa/ 100) * tempoemdias)
print("O valor da prestação e R$", prestacao)
