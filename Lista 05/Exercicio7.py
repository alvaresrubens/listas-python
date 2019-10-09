palavra = input ("Digite uma palavra: ")
palavra = palavra.lower()

if len(palavra)%2 != 0:
    print ("Quantidade par de letras da palavra ", palavra , ":", len(palavra))
    print ("Indice da letra central:", len(palavra)//2)
    central = palavra [len(palavra)//2]
    if central =='a' or central =='e ' or central =='i' or central =='o 'or central =='u':
        print ("A letra central", central, "é vogal")
    else:
        print ("A letra central", central, "não é vogal")
else:
    print ("Indice da letra central:", len(palavra)//2)
    central = palavra [len(palavra)//2] + palavra [(len(palavra)//2)-1]
    if central =='rr' or central =='ss ':
        print ("A letras centrais formam dígrafo", central)
    else:
        print ("A letra central", central, "não formam dígrafo rr ou ss")

