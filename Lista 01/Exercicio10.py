salarioMin = float(input("Qual é o valor do salário mínimo (em reais)?: "))
salario = float(input("Qual é o valor do salário da pessoa (em reais)?: "))

print("A pessoa em questão ganha {0:.3f}".format(salario/salarioMin) + " salários mínimos.")