notas = [3.0,4.0,5.0,6.0,3.0]

maiorNota = max(notas)
print(str(maiorNota))

for nota in notas:
    print("Nota anterior: ", nota,"> Nota Ponderada:",(nota*10)/maiorNota)