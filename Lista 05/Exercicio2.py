capital = input("Qual a capital do Brasil? ")


if len(capital) != 8:
    print ("Resposta incorreta.")

else:

    capital = capital.lower()   
    capital = capital.replace("á","a")
    capital = capital.replace("â","a")
    capital = capital.replace("ã","a")
    capital = capital.replace("à","a")
    capital = capital.replace("í","i")
    capital = capital.replace("ì","i")
    if "brasilia" in capital:
        print ("Resposta correta")
    else:
        print ("Resposta incorreta")
    
    



