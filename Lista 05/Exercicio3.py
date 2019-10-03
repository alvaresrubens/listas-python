import math

numero = int (input("Digite um número real:"))
resultado = 0
operacao = ""

if numero<0:
    resultado = numero*numero
    operacao = "Quadrado de: "
else:
    resultado = format (math.sqrt(numero), '.5f')
    operacao = "Raiz quadrada de:"

print (operacao, numero, resultado)
concatenacao = (str (numero)).replace(".","")+ (str (resultado)).replace(".","")
concatenacao =  concatenacao.replace ("", "-")
print ("Concatenação: ", concatenacao )