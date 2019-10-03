
var1 = float(input("Digite o valor de var1: "))
var2 = float(input("Digite o valor de var2: "))
print("Valor de var1 antes da troca: {0:010.4f} ".format(var1))
print("Valor de var2 antes da troca: {0:010.4f} ".format(var2))
aux = var2
var2 = var1
var1 = aux
print("Valor de var1 DEPOIS da troca: {0:010.4f} ".format(var1))
print("Valor de var2 DEPOIS da troca: {0:010.4f} ".format(var2))
