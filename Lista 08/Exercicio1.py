atletas_mirins = {1:[10,1.40], 
                  2:[11,1.55],
                  3:[15,1.70], 
                  4:[17,1.80],
                  5:[12,1.50],
                  6:[11,1.62], 
                  7:[13,1.73],
                  8:[16,1.85],
                  9:[12,1.57], 
                  10:[14,1.60]}

count_idade = 0
count_altura =0

for atleta in atletas_mirins.values():
    count_idade = count_idade +atleta[0]
    count_altura = count_altura+atleta[1]

media_altura = count_altura/len(atletas_mirins)
media_idade = count_idade/len(atletas_mirins)

lista_resultado = []
for atleta in atletas_mirins.values():
    if atleta[0]<16 and atleta[1]>media_altura:
        lista_resultado.append(atleta)

for atleta in atletas_mirins:
    
    print(atletas_mirins[atleta])  

print("Média de altura dos atletas mirins: ", media_altura )
print("Média de idade dos atletas mirins: ", media_idade )
print("Menos de 16 anos e acima da média de altura", lista_resultado )

