nomeP1 = input("Digite o nome do produto 1: ")
precoP1 = float(input("Digite o preço do produto 1 (em reais): "))
unidadesP1 =float(input("Quantas unidades do produto 1 foram compradas? " ))
nomeP2 = input("Digite o nome do produto 2: ")
precoP2 = float(input("Digite o preço do produto 2 (em reais): "))
unidadesP2 =float(input("Quantas unidades do produto 2 foram compradas? " ))
nomeP3 = input("Digite o nome do produto 3: ")
precoP3 = float(input("Digite o preço do produto 3 (em reais): "))
unidadesP3 =float(input("Quantas unidades do produto 3 foram compradas? " ))
nomeP4 = input("Digite o nome do produto 4: ")
precoP4 = float(input("Digite o preço do produto 4 (em reais): "))
unidadesP4 =float(input("Quantas unidades do produto 4 foram compradas? " ))
nomeP5 = input("Digite o nome do produto 5: ")
precoP5 = float(input("Digite o preço do produto 5 (em reais): "))
unidadesP5 =float(input("Quantas unidades do produto 5 foram compradas? " ))

calculado1 = precoP1*unidadesP1
calculado2 = precoP2*unidadesP2
calculado3 = precoP3*unidadesP3
calculado4 = precoP4*unidadesP4
calculado5 = precoP5*unidadesP5
totalCompra = calculado1+calculado2+calculado3+calculado4+calculado5


print("*************\nLista de produtos \n*************\n1){nomeP1} (R${precoP1} - {unidadesP1} unidade(s)): R${total1})\n2){nomeP2} (R${precoP1} - {unidadesP2} unidade(s)): R${total2})\n3){nomeP3} (R${precoP1} - {unidadesP3} unidade(s)): R${total3})\n4){nomeP4} (R${precoP1} - {unidadesP4} unidade(s)): R${total4})\n5){nomeP5} (R${precoP5} - {unidadesP5} unidade(s)): R${total5}) \nTotal da compra: R${totalFinal} \n************".format(nomeP1=nomeP1, precoP1=precoP1,unidadesP1=unidadesP1, total1='%0.2f' %calculado1, nomeP2=nomeP2, precoP2=precoP2,unidadesP2=unidadesP2, total2='%0.2f' %calculado2, nomeP3=nomeP3, precoP3=precoP3,unidadesP3=unidadesP3, total3='%0.2f' %calculado3, nomeP4=nomeP4, precoP4=precoP4,unidadesP4=unidadesP4, total4='%0.2f' %calculado4,nomeP5=nomeP5, precoP5=precoP5,unidadesP5=unidadesP5, total5='%0.2f' %calculado5, totalFinal='%0.2f' %totalCompra))
        

