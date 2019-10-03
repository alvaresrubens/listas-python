num1= int( input ("Por favor, digite o primeiro número: ") )
num2= int( input ("Por favor, digite o segundo número: ") )
num3= int( input ("Por favor, digite o terceiro número: ") )
rest= (num1*num2)%num3

print("Multiplicação de "+str(num1)+" por "+str(num2)+": "+ str(num1*num2))
print("Resto da divisão entre "+str(num1*num2)+" por "+str(num3)+": "+ str(rest))