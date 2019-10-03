
pesokg = float(input("Qual é o peso da pessoa (em quilos)? "))
pesogr = pesokg*1000
engorda = (pesokg*0.12) + pesokg
print("A pessoa em questão pesa {0:.2f}".format(pesogr))
print("Se ela engordar 12% passará a pesar {0:.2f}".format(engorda) + " quilos")
