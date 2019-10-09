from unicodedata import normalize

texto1 = input("Digite um texto: ")
texto2 = input("Digite outro texto: ")

espacos1 = 0
espacos2 = 0
virgulas1 = 0
virgulas2 = 0
pontos1 = 0
pontos2 = 0
letras1 = 0
letras2 = 0

for caractere1 in texto1:
    if(caractere1 == " "):
        espacos1= espacos1+1
    if(caractere1 == ","):
        virgulas1=virgulas1+1
    if(caractere1 == "."):
        pontos1= pontos1+1

letras1 = len(texto1) - espacos1 - virgulas1 - pontos1

for caractere2 in texto2:
    if(caractere2 == " "):
        espacos2= espacos2 +1
    if(caractere2 == ","):
        virgulas=virgulas2 +1
    if(caractere2 == "."):
        pontos2 =pontos2 +1

letras2 = len(texto2) - espacos2 - virgulas2 - pontos2


if texto1 in texto2:
    mensagem1 = "Os dois textos são idênticos se considerarmos todos os caracteres"
else: 
    mensagem1 = "Os dois textos não são idênticos se considerarmos todos os caracteres"

normalizado1 = normalize('NFKD', texto1).encode('ASCII','ignore').decode('ASCII')
normalizado2 = normalize('NFKD', texto2).encode('ASCII','ignore').decode('ASCII')
normalizado1 = normalizado1.replace(",","")
normalizado1 = normalizado1.replace(".","")
normalizado2 = normalizado1.replace(",","")
normalizado2 = normalizado1.replace(".","")
normalizado1 = normalizado1.lower()
normalizado2 = normalizado2.lower()

if normalizado1 in normalizado2:
    mensagem2 = "Se considerarmos apenas as letras, os dois textos são identicos"
else: 
    mensagem2 = "Se considerarmos apenas as letras, os dois textos não são identicos"


print("Primeiro texto:", texto1)
print("Segundo texto:", texto2)
print("O primeiro texto possui:", len(texto1),"caractere(s)",letras1,"letra(s)",espacos1,"espaço(s)", virgulas1,"vírgulas e", pontos1,"ponto(s)")
print("O segundo texto possui:", len(texto2),"caractere(s)",letras2,"letra(s)",espacos2,"espaço(s)", virgulas2,"vírgulas e", pontos2,"ponto(s)")
print(mensagem1)
print(mensagem2)
print("Letras do primeiro texto, invertidas:", texto1[::-1])
print("Letras do segundo texto, invertidas:", texto2[::-1])
print("Letras do primeiro texto, invertidas e minúsculas:", texto1[::-1].lower())
print("Letras do segundo texto, invertidas e minúsculas:", texto2[::-1].lower())