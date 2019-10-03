
somaFor = 0

for contador in range (0,1000,1):
    y= int(input("Digite um número inteiro (0 para sair): "))
    if y == 0:
        break
    else:
        somaFor = somaFor+y
print("Foram digitados", contador,"número(s)")
print("Soma dos números digitados:", somaFor)
print("Média dos números digitados:", somaFor/contador)
    
