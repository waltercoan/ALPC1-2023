'''
2)	Construir um programa que efetue o cálculo 
do salário líquido de um professor. Para fazer 
este programa, você deverá possuir alguns dados, 
tais como: valor da hora aula, número de horas 
trabalhadas no mês e percentual de desconto do 
INSS. Em primeiro lugar, deve-se estabelecer
qual será o seu salário bruto para efetuar o 
desconto e ter o valor do salário líquido.
'''
#entradas
print("Digite o valor da hora aula")
valhora = float(input())
print("Digite o numero de horas trabalhadas")
numhoras = int(input())
print("Digite o percentual do desconto do inss")
percdesc = float(input())
#processamento
salbruto = valhora * numhoras
print("Salario bruto", salbruto)
valimpto = (salbruto * percdesc) / 100
print("Valor imposto", valimpto)
salliq = salbruto - valimpto
#saida
print("O salario liquido e ", salliq)