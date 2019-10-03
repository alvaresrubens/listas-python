nome1, preco1, quantidade1 = input ("Digite nome, preço e quantidade do produto 1, separados por vírgula: ").split(",")
nome2, preco2, quantidade2 = input ("Digite nome, preço e quantidade do produto 2, separados por vírgula: ").split(",") 
nome3, preco3, quantidade3 = input ("Digite nome, preço e quantidade do produto 3, separados por vírgula: ").split(",") 
nome4, preco4, quantidade4 = input ("Digite nome, preço e quantidade do produto 4, separados por vírgula: ").split(",") 
nome5, preco5, quantidade5 = input ("Digite nome, preço e quantidade do produto 5, separados por vírgula: ").split(",") 

preco1 = float(preco1)
preco2 = float(preco2)
preco3 = float(preco3)
preco4 = float(preco4)
preco5 = float(preco5)

quantidade1 = int(quantidade1)
quantidade2 = int(quantidade2)
quantidade3 = int(quantidade3)
quantidade4 = int(quantidade4)
quantidade5 = int(quantidade5)

total1= preco1*quantidade1
total2= preco2*quantidade2
total3= preco3*quantidade3
total4= preco4*quantidade4
total5= preco5*quantidade5

unidade1= "unidade"
unidade2= "unidade"
unidade3= "unidade"
unidade4= "unidade"
unidade5= "unidade"


if quantidade1>=12:
    total1= total1 - (total1 * 0.2)
if quantidade2>=12:
    total2= total2 - (total2 * 0.2)
if quantidade3>=12:
    total3= total3 - (total3 * 0.2)
if quantidade4>=12:
    total4= total4 - (total4 * 0.2)
if quantidade5>=12:
    total5= total5 - (total5 * 0.2)

if quantidade1>1:
    unidade1 = "unidades"
if quantidade2>1:
    unidade2 = "unidades"
if quantidade3>1:
    unidade3 = "unidades"
if quantidade4>1:
    unidade4 = "unidades"
if quantidade5>1:
    unidade5 = "unidades"

totalGeral= total1+total2+total3+total4+total5

print ("################")
print ("Nota de compras")
print ("################")
print ("\t 1)", nome1,"(R$",preco1,")",quantidade1,unidade1,": R$",total1)
print ("\t 2)", nome2,"(R$",preco2,")",quantidade2,unidade2,": R$",total2)
print ("\t 3)", nome3,"(R$",preco3,")",quantidade3,unidade3,": R$",total3)
print ("\t 4)", nome4,"(R$",preco4,")",quantidade4,unidade4,": R$",total4)
print ("\t 5)", nome5,"(R$",preco5,")",quantidade5,unidade5,": R$",total5)
print ("Total da compra: R$",'%0.2f'%totalGeral)
print ("################")
