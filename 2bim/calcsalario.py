'''
1)	Faça um programa que receba o número de horas trabalhadas, 
o valor do salário mínimo e o número de horas extras trabalhadas.
Calcule e mostre o salário a receber seguindo as regras abaixo:
a)	a hora trabalhada vale 1/8 do salário mínimo;
b)	a hora extra vale ¼ do salário mínimo;
c)	o salário bruto equivale ao número de horas trabalhadas 
multiplicado pelo valor da hora trabalha (apresente o valor para o usuário);
d)	a quantia a receber pelas horas extras equivale ao 
número de horas extras trabalhadas multiplicado pelo valor 
da hora extra(apresente o valor para o usuário);
e)	o salário a receber equivale ao salário bruto mais a 
quantia a receber pelas horas extras(apresente o valor para o usuário);
'''
#entradas
print("Digite o numero de horas trab")
numhoras = int(input())
print("Digite o valor do salario minimo")
valsalmin = float(input())
print("Digite o num de horas extras")
numhorasextras = int(input())
#processamento
valhora = valsalmin / 8
print("Valor da hora e ", valhora)
valhoraextra = valsalmin / 4
print("Valor da hora extra e ", valhoraextra)
salbruto = numhoras * valhora
print("O salario bruto e ", salbruto)
tothoraextra = valhoraextra * numhorasextras
print("O total das horas extras e", tothoraextra)
salarioreceber = salbruto + tothoraextra
print("O salario a receber e ", salarioreceber)