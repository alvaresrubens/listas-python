int1, int2, int3 = input("Digite três números inteiros, separados por espaço: ").split(" ")
a = int(int1)
b= int(int2)
c = int(int3)
triangulo = False


if a+b>c and a+c>b and b+c>a:
    triangulo = True

if triangulo == True:
    print("As três medidadas lidas se configuram como lados de um triângulo")
else:
    print("As três medidadas lidas não configuram como lados de um triângulo")