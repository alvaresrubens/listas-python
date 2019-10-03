valido = False

while valido== False:
    valor = int(input("Entre com um valor inteiro em reais: "))
    if valor >0:
        valido = True

if valor%50 !=0:
    if valor//50 >1:
        print(valor//50, "s de 50 reais")
        valor =  valor - (valor//50)* 50
else:
    print(valor//50, "cédula de  50 reais"  )
    valor =  valor - (valor//50)* 50

if valor%20 !=0:
    if valor//20 >1:
        print(valor//20, "cédulas de 20 reais")
        valor =  valor - (valor//200)* 20
else:
    print(valor//20, "cédula de  20 reais"  )
    valor =  valor - (valor//20)* 20

if valor%10 !=0:
    if valor//10 >1:
        print(valor//10, "cédulas de 10 reais")
        valor =  valor - (valor//10)* 10
else:
    print(valor//10, "cédula de  10 reais"  )
    valor =  valor - (valor//10)* 10

if valor%5 !=0:
    if valor//5 >1:
        print(valor//5, "cédulas de 5 reais")
        valor =  valor - (valor//5)* 5
else:
    print(valor//5, "cédula de  5 reais"  )
    valor =  valor - (valor//5)* 5

if valor%2 !=0:
    if valor//2 >1:
        print(valor//2, "cédulas de 2 reais")
        valor =  valor - (valor//2)* 2
else:
    print(valor//2, "cédula de  2 reais"  )
    valor =  valor - (valor//2)* 2

if valor%1 !=0:
    if valor//1 >1:
        print(valor//1, "cédulas de 1 reais")
        valor =  valor - (valor//1)* 1
else:
    print(valor//1, "cédula de  1 reais"  )
    valor =  valor - (valor//1)*1