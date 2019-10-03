sexo = input("Digite o sexo da pessoa ('M' ou 'F'): ")

if sexo == "M" or sexo == "m":
    nome = input("Digite o nome do aluno: ")
    sexoExtenso= "O aluno"
    
else:
    if sexo == "F" or sexo =="f":
        nome = input("Digite o nome da aluna: ")
        sexoExtenso= "A aluna"
        

n1,n2,n3,n4,n5 = input ("Digite as notas finais das 5 matérias, separadas por ponto-e-vírgula: ").split(";")
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
n5 = float(n5)

if n1 and n2 and n3 and n4 and n5 >=7:
    print(sexoExtenso, nome, "foi aprovado(a) no ano letivo.")
else:
    print(sexoExtenso, nome, "foi reprovado(a) no ano letivo.")