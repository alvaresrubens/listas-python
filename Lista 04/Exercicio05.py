inteiro = int(input("Digite um número inteiro: "))
x=1
print("Método em While")
while x<11:
    print(inteiro,"+", x, "=",x+inteiro)
    x+=1
print("Método em For")
for y in range (1,11,1):
    print(inteiro,"+", y, "=",y+inteiro)