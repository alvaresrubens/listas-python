texto = input("Digite um texto ")
mensagem = ""


for letra in texto:
    print("O caractere", letra, "aparece", texto.count(letra), "vezes")
