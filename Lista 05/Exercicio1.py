numero = int (input("Digite um número real: "))
if numero<0:
    sinal = "negativo"
else:
    sinal = "positivo"

numero = format(numero)
print (numero)
digitos = 0

for digito in numero:
    if(digito !="." and digito !="-"):
        digitos = digitos + 1

if (digitos> 1):
    quantidade = "dígitos númericos"
else:
    quantidade = "dígito númerico"

print ("O número", numero, "é", sinal, "e contém ", digitos, quantidade)