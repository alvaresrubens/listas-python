inteiro = int (input("Digite um número inteiro: "))
multiplo7= "não é múltiplo"
multiplo13= "não é múltiplo"
multiplo55 = "não é múltiplo"

if inteiro%7 == 0:
    multiplo7 = "é múltiplo"
if inteiro%13 == 0:
    multiplo13 = "é múltiplo"
if inteiro%55 == 0:
    multiplo55 = "é múltiplo"

print ("O número", inteiro, multiplo7, "de 7,", multiplo13, "de 13,", multiplo55, "de 55.")