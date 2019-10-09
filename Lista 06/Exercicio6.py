texto_base = input("Digite um texto-base: ")
replace_base = input("Digite um grupo de caracteres a serem substituidos: ")
insert_base = input("Digite um grupo de caracteres com novos caracteres que possua mesmo número de caracteres do grupo de substituição: ")
indice = 0
for indice in texto_base:
    texto_base = texto_base.replace(replace_base[indice],insert_base[indice])
