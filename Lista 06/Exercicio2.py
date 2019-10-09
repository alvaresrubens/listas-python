texto = input("Digite um texto ")
busca = input("Digite outro texto ")
intersecao = ""
for letra in busca:
    if letra in texto:
        intersecao = intersecao + letra
        
if intersecao == "":
    print ("Não existem caracteres comuns aos dois textos")
else:
    print ("Os caracteres em comum aos dois textos são:", intersecao)
