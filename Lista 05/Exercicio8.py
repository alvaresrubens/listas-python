entrada = input ("Digite um texto de 5 caracteres: ")
if len(entrada) != 5:
    print ("O texto digitado não possui 5 caracteres")
else:
    
    opcao = input ("Digite 1 para retornar todas as letras em minúsculas \nDigite 2 para retornar todas as letras em  maiúsculas \nDigite -1 para sair do programa: ")
    print ("Opcão escolhida: ", opcao)
    if opcao == "1":
        print (entrada.lower())
    elif opcao =="2":
        print (entrada.upper())
    elif opcao == "-1":
        print ("Programa finalizado")
   