temperatura = int(input("Digite a temperatura a ser convertida (em graus): "))
print("**************")
print("Operações de Conversão:")
print("\t1:Celsius para Fahrenheit")
print("\t2:Celsius para Kelvin")
print("\t3:Fahrenheit para Celsius")
print("\t4:Fahrenheit para Kelvin")
print("\t5:Kelvin para Fahrenheit")
print("\t6:Kelvin para Celsius")
print("**************")
operador =int (input("Digite a operaçao de conversão: "))

if operador == 1:
    convertido = ((9/5)*temperatura)+32
    print("Resposta: {entrada} graus Celsius equivalem a {resultado} Fahrenheit".format(entrada =temperatura, resultado=convertido))
if operador == 2:
    convertido = temperatura+273
    print("Resposta: {entrada} graus Celsius equivalem a {resultado} Kelvin" .format(entrada =temperatura, resultado=convertido))
if operador == 3:
    convertido = ((5/9)*temperatura)-32
    print("Resposta: {entrada} graus Fahrenheit equivalem a {resultado} Celsius".format(entrada =temperatura, resultado=convertido))
if operador == 4:
    convertido = (((5/9)*temperatura)-32)+273
    print("Resposta: {entrada} graus Fahrenheit equivalem a {resultado} Kelvin".format(entrada =temperatura, resultado=convertido))
if operador == 5:
    convertido = (((9/5)*temperatura)-273)+ 32
    print("Resposta: {entrada} graus Kelvin equivalem a {resultado} Fahrenheit".format(entrada =temperatura, resultado=convertido))
if operador == 6:
    convertido = temperatura-273
    print("Resposta: {entrada} graus Kelvin equivalem a {resultado} Celsius".format(entrada =temperatura, resultado=convertido))