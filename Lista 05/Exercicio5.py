import math

inteiro = int (input("Digite um número inteiro: "))

if inteiro%2 == 0 and inteiro%5 == 0 and inteiro%10 == 0:
    print ("O número", inteiro, "é múltiplo de 10, de 5  e de 2")
else:
    print ("O número", inteiro, "é não múltiplo de 10, nem de 5, nem de 2")
    print ("Os 15 primeiros dígitos do fatorial de", inteiro, "são:", '%0.15s' %math.factorial(inteiro))
    print ("O log na base 10 de", inteiro, "é:", '%.015s' %math.log10(inteiro))
