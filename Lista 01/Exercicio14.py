carros = int(input("Quantos carros foram vendidos no mês? "))
valorVendas = float(input("Qual foi o valor total das vendas (em reais)? "))
salarioFixo = float(input("Qual é o salário fixo do vendedor (em reais)? "))
valorFixo = float(input("Qual é o valor fixo que o endendor recebe por cada carro vendido (em reais)? "))

print("Neste mês, o vendedor irá receber R$ {0:.2f}.".format(salarioFixo+(carros*valorFixo)+valorVendas*0.05))