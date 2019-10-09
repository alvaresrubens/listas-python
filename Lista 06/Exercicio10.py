texto1 = input("Digite um texto: ")


for caractere in texto1:
    print(texto1)
    texto1= texto1.replace(texto1[len(texto1)-1],"")
    