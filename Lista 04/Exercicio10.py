valido = False

while valido== False:
    valor = float(input("Entre com um valor inteiro em reais: "))
    if valor >0:
        valido = True
    else:
        print ("É necessário que você digite um valor positivo, diferente de zero")

if valor%100 !=0:
    if valor//100 >1:
        print(valor//100, "cédulas de 100 reais")
        valor =  valor - (valor//100)* 100
else:
    print(valor//100, "cédula de  100 reais"  )
    valor =  valor - (valor//100)* 100

if valor%50 !=0:
    if valor//50 >1:
        print(valor//50, "cédulas de 50 reais")
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

if valor%0.50 !=0:
    if valor//0.50 >1:
        print(valor//0.50, "moedas de 50 centavos")
        valor =  valor - (valor//0.50)* 0.50
else:
    print(valor//0.50, "moeda de 50 centavos"  )
    valor =  valor - (valor//0.50)*0.50

if valor%0.10 !=0:
    if valor//0.10 >1:
        print(valor//0.10, "moedas de 10 centavos")
        valor =  valor - (valor//0.10)* 0.10
else:
    print(valor//0.10, "moeda de 10 centavos"  )
    valor =  valor - (valor//0.10)*0.10

if valor%0.05 !=0:
    if valor//0.05 >1:
        print(valor//0.05, "moedas de 5 centavos")
        valor =  valor - (valor//0.05)* 0.05
else:
    print(valor//0.50, "moeda de 5 centavos"  )
    valor =  valor - (valor//0.05)*0.05

if valor%0.02 !=0:
    if valor//0.02 >1:
        print(valor//0.02, "moedas de 2 centavos")
        valor =  valor - (valor//0.02)* 0.02
else:
    print(valor//0.02, "moeda de 2 centavos"  )
    valor =  valor - (valor//0.02)*0.02

if valor%0.01 !=0:
    if valor//0.01 >1:
        print(valor//0.01, "moedas de 1 centavo")
        valor =  valor - (valor//0.01)* 0.01
else:
    print(valor//0.01, "moeda de 1 centavo"  )
    valor =  valor - (valor//0.01)*0.01
       
       
       
       
