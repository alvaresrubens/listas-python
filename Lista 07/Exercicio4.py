lista1 = input ("Digite 10 numeros separados por ponto e virgula: ").split(";")
lista1 = list (lista1)
lista2 = input ("Digite outros 10 numeros separados por ponto e virgula: ").split(";")
lista2 = list (lista2)

listaComum = []
listaExclusivo = []

for numero in lista1:
    if numero in lista2:
        listaComum.append(numero)
    else:
        listaExclusivo.append(numero)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Números em comum:", listaComum)
print("Números exclusivos:", listaExclusivo)