
contador = 0
soma = 0
sair = False

print("Versão While")
while sair== False:
    x = int(input("Digite um número inteiro (0 para sair): "))
    if x==0:
        sair= True
    else:
        contador+=1
        soma = soma +x

print("Foram digitados", contador,"número(s)")
print("Soma dos números digitados:", soma)
print("Média dos números digitados:", soma/contador)

print("\nVersão For")

contadorFor=0
somaFor = 0
sairFor= False

for contadorFor in range (0, sairFor == True, 1):
    y= int(input("Digite um número inteiro (0 para sair): "))
    if y == 0:
        sairFor = True
    else:
        contadorFor+=1
        somaFor = somaFor+y

print("Foram digitados", contadorFor,"número(s)")
print("Soma dos números digitados:", somaFor)
print("Média dos números digitados:", somaFor/contadorFor)
    
