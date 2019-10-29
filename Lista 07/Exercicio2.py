inferior = int (input("Digite o limite inferior: "))
superior = int (input("Digite o limite superior: "))
lista = [-72,12,2,7,16,-18,20-24,26,0,32,15,38]
lista.sort()
listaFinal = []

for numero in lista:   
    if numero>=inferior and numero<=superior:
        listaFinal.append(numero)
    

print ("Resultado", listaFinal)