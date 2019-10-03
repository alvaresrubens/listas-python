c = float(input("Digite o valor da conta sem taxas (em R$): "))
i = 0.05  # Taxa de imposto de 5%
t = 0.10  # Taxa de serviço de 10%
r = ((c*i) + (c*t)) + c

print(f'Valor inicial da conta: R$ {c:.2f}')
print(f'Impostos: R$ {c*i:.2f}')
print(f'Taxa: R$ {c*t:.2f}')
print(f'Valor final da conta: R$ {r:.2f}')
