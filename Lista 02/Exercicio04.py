import math
n1 = float (input("Por favor, digite o primeiro número real: "))
n2 = float (input("Por favor, digite o segundo número real: "))
n3 = float (input("Por favor, digite o terceiro número real: "))
n4 = float (input("Por favor, digite o quarto número real: "))

aux1= n1+n3
aux2= n2+n4
multi = aux1*aux2
total = math.sqrt(multi)

print(f"Operações efetuadas:\n {n1}+{n3} = {aux1} \n {n2}+{n4} = {aux2} \n {aux1}*{aux2} = {multi}\n Raiz Quadrada de {multi} = {'%.4f'%total}")

