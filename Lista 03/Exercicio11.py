int1,int2,int3 = input("Digite três números inteiros diferentes entre si e separados por espaço: ").split(" ")

a = int(int1)
b = int(int2)
c = int(int3)

if a>=b and a>=c:
    maior = a
    menores = b+c
elif b>=a and b>=c:
    maior = b
    menores = a+c
else:
    maior = c
    menores = a+b
if a<b and a<c:
    menor = a
elif b<=a and b<=c:
    menor = b
else:
    menor = c   

if a<b and a>c:
    meio = a
elif b<a and b>c:
    meio = b
elif c<a and c>b:
    meio = c


print ("Menor número:", menor)
print ("Maior número:", maior)
print ("Soma dos dois menores:", menores)
print ("Números lidos em ordem crescente:",menor,",",meio, ",",maior)