texto = input("Digite um texto ")
busca = input("Digite outro texto ")
disjuncao = ""
for letra in busca:
    if letra not in texto:
        disjuncao = disjuncao + letra

for letra in texto:
    if letra not in busca:
        disjuncao = disjuncao + letra

if disjuncao == "":
    print ("Não existem caracteres comuns aos dois textos")
else:
    print ("Os caracteres que aparecem em apenas um dos dos textos são:", disjuncao)
