eleitores = int(input("Qual é o número total de eleitores do município? "))
votos = int(input("Qual é o número total de votos válidos? "))
brancos = int(input("Quantas pessoas votaram em branco? "))
nulos = int(input("Quantas pessoas votaram em nulo? "))

print("Percentual de votos válidos: {0:.2f}".format(votos/eleitores*100)+"%")
print("Percentual de votos em branco: {0:.2f}".format(brancos/eleitores*100)+"%")
print("Percentual de votos nulos: {0:.2f}".format(nulos/eleitores*100)+"%")