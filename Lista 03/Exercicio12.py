horas = int(input("Quantas horas foram trabalhadas no mês? "))
salarioHora = float (input("Qual é o salário por hora (em reais)? "))


if horas>160:
    horasExtras = horas-160
    valorExtra = horasExtras*(salarioHora*0.5)
    salarioTotal = (horas*salarioHora)+valorExtra
else:
    salarioTotal = salarioHora * horas

print("Neste mês, o funcionário receberá R$",'%0.2f'%salarioTotal,"de salário")