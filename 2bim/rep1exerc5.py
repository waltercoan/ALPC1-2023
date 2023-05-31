'''
REPETIÇÃO5) Elaborar um programa 
que apresente os valores de 
conversão de graus Celsius em 
Fahrenheit, de 10 em 10 graus, 
iniciando a contagem em 10 graus 
Celsius e finalizando em 100 
graus Celsius. O programa 
deverá apresentar os valores 
das duas temperaturas.
'''
cel = 10
while cel <= 100:
    fah = (cel * 9/5) + 32
    #String Interpolation
    print(f"Celsius {cel} - Fahrenheit {fah}")
    #print("Celsius", cel, "- Fahrenheit",fah)
    cel += 10
    #cel = cel + 10

