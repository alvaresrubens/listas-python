texto = input("Digite um texto-base: ")
busca = input("Digite um texto com caracteres a serem retirados: ")

for caractere in texto:
    texto = texto.replace(busca, "")
print  ("O texto restante após a retirada é:", texto.strip())
