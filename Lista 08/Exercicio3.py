frase = input ("Digite uma frase a ser analisada: ")
lista1 = []
lista2 = []

for letra in frase:
    lista1.append(letra)
    lista2.append(frase.index(letra))

lista3 = zip (lista1, lista2)
dicionario = dict(lista3)

print(dicionario)
