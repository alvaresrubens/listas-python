texto = input("Digite um texto ")
mensagem = ""

for letra in texto:
    
    print("O caractere", letra, "aparece", letra.count(texto), "vezes")
