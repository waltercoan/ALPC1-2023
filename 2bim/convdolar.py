'''
1)	Elaborar um programa que efetue
 o cálculo do valor da conversão 
 em real (R$) de um valor lido em 
 tela em dólar (US$). O programa 
 deverá solicitar o valor da 
 cotação do dólar.
ENTRADAS
 - VALORDOLAR
 - VALORCOTAC
PROCESSAMENTO
  VALORREAIS =  VALORDOLAR * VALORCOTAC
SAIDA
 - VALORREAIS
'''
#ENTRADAS
print("Digite o valor em dolar")
#float são numeros decimais
valordolar = float(input())
print("Digite o valor da cotação")
valorcotac = float(input())
#PROCESSAMENTO
valorreais = valordolar * valorcotac
print(f"O valor em reais e R$ {valorreais}")
