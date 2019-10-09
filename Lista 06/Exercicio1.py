texto = input("Digite um texto ")
busca = input("Digite outro texto ")

if busca in texto:

    print ("hello world")
    print("O texto: ", busca, "ocorre ",texto.count(busca), "no texto:  ", texto)
    indice = 0
    while (indice >-1):
        indice = texto.find(busca, indice)
        if(indice >=0):
            print ("o texto:",busca,"foi encontrado na posição", indice, "do texto:", texto  )
            indice = indice+1
    
else:
    print("O texto:", busca,"não ocorre dentro de texto:  ", texto)    
