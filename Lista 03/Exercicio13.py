n1 = float (input("Por favor, digite o primeiro operando: "))
n2 = float (input("Por favor, digite o segundo operando: "))
print("***************")
print("Operações Aritméticas:")
print("\t1) Adicação")
print("\t2) Subtração")
print("\t3) Divisão")
print("\t4) Multiplicação")
print("\t5) Exponênciação")
print("\t6) Resto da divisão")
print("\t7) Quociente da divisão")

op = int(input("Por favor, digite a operação: "))

if op == 1:
    resultado=n1+n2
    operador="+"
if op == 2:
    resultado=n1-n2
    operador="-"
if op == 3:
    resultado=n1/n2
    operador="/"
if op == 4:
    resultado=n1*n2
    operador="*"
if op == 5:
    resultado=n1**n2
    operador="^"
if op == 6:
    resultado=n1%n2
    operador="%"
if op == 7:
    resultado=n1//n2
    operador="//"

print("Resultado:",n1,operador,n2,"=",'%0.2f'%resultado)