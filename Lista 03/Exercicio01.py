consumo = float (input("Digite a quantidade de energia elétrica consumida (em kWh): "))
tipo = input("Digite o tipo de instalação ('R' para residencial; 'C' para comercial; 'I' para industrial): ") 
residencial = "R"
comercial = "C"
industrial = "I"

if tipo == residencial:
    if consumo <= 500:
        consumoTotal = consumo * 0.40
        print ("Preço a pagar pela energia consumida: R${consumoPrint}".format(consumoPrint= '%0.2f'%consumoTotal))
    else:
        consumoTotal = consumo * 0.65
        print ("Preço a pagar pela energia consumida: R${consumoPrint}".format(consumoPrint= '%0.2f'%consumoTotal))
elif tipo == comercial:
    if consumo <= 1000:
        consumoTotal = consumo * 0.55
        print ("Preço a pagar pela energia consumida: R${consumoPrint}".format(consumoPrint= '%0.2f'%consumoTotal))
    else:
        consumoTotal = consumo * 0.60
        print ("Preço a pagar pela energia consumida: R${consumoPrint}".format(consumoPrint= '%0.2f'%consumoTotal))
elif tipo == industrial:
    if consumo <= 5000:
        consumoTotal = consumo * 0.55
        print ("Preço a pagar pela energia consumida: R${consumoPrint}".format(consumoPrint= '%0.2f'%consumoTotal))
    else:
        consumoTotal = consumo * 0.60
        print ("Preço a pagar pela energia consumida: R${consumoPrint}".format(consumoPrint= '%0.2f'%consumoTotal))       