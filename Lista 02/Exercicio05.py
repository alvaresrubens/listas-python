n1 = float (input("Por favor, digite o primeiro número: "))
n2 = float (input("Por favor, digite o segundo número: "))
n3 = float (input("Por favor, digite o terceiro número: "))
n4 = float (input("Por favor, digite o quarto número: "))
n5 = float (input("Por favor, digite o qufloato número: "))
n6 = float (input("Por favor, digite o sexto número: "))

aux1= n1+n2
aux2= n4-n3
aux3= n5/n6
total= aux1*aux2*aux3

print("Operações efetuadas:\n",n1,"+",n2,"=",aux1, "\n",n4,"-",n3,"=",aux2,"\n",n5,"/",n6,"=",aux3,"\nResultado final da multiplicação dos três resultados anteriores",'%015.3f'%total)


