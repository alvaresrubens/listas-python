lista = [55,37,12,25,95,2]
contador = 0

for numero in lista:
    contador = contador + numero

media = contador/len(lista)
print (media)

menorDiferenca = 0 
numeroMaisProximo = 0 

for numero in lista:
    diferenca = numero - media
    if diferenca <0:
        diferenca = diferenca*-1
    if menorDiferenca == 0 or diferenca<menorDiferenca:
        numeroMaisProximo = numero
        menorDiferenca = diferenca

print(numeroMaisProximo) 