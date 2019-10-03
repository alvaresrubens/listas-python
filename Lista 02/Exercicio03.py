n1 = int (input("Por favor, digite o primeiro número: "))
n2 = int (input("Por favor, digite o segundo número: "))
n3 = int (input("Por favor, digite o terceiro número: "))
n4 = int (input("Por favor, digite o quarto número: "))
n5 = int (input("Por favor, digite o quinto número: "))
n6 = int (input("Por favor, digite o sexto número: "))
n7 = int (input("Por favor, digite o sétimo número: "))
n8 = int (input("Por favor, digite o oitavo número: "))

aux= n1+n2+n3+n4+n5+n6

print("Operações efetuadas: \n {r1}+{r2}+{r3}+{r4}+{r5}+{r6}= {res} \n {res}-{r7}-{r8}={final}".format(r1="%.2f"%n1,r2=n2,r3=n3,r4=n4,r5=n5,r6=n6,r7=n7,r8=n8,res=aux, final=aux-n7-n8)) 