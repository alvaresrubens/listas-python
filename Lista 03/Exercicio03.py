valorCasa = float (input("Por favor, digite o valor de compra da casa (em reais): "))
salario = float (input("Por favor, digite o salário): "))
anos = float (input("Em quantos anos você pretende financiar? "))
meses = anos*12
teto = salario*0.3
prestacao = valorCasa/meses
concedido = "concedido."
nconcedido = "não concedido."

if prestacao <= teto:
    resultado = concedido
else:
    resultado = nconcedido

print ("Teto da prestação: R${valorTeto}".format(valorTeto='%0.2f'%teto))
print ("Prestação: R${valorPrestacao}".format(valorPrestacao='%0.2f'%prestacao))
print ("Empréstimo",resultado)

