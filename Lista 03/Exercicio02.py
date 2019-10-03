print ("Você deverá digitar 3 números inteiros")
a = int (input(" Por favor, digite o primeiro número inteiro: "))
b = int (input(" Por favor, digite o segundo número inteiro: "))
c = int (input(" Por favor, digite o terceiro número inteiro: "))

maior = 0
menor = 0

if a>=b and a>=c:
    maior = a
elif b>=a and b>=c:
    maior = b
else:
    maior = c

if a<=b and a<=c:
    menor = a
elif b<=a and b<=c:
    menor = b
else:
    menor = c    

print("Menor:", str(menor), "\nMaior:", str(maior))   