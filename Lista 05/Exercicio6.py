from unicodedata import normalize

nome = input("Digite o nome de uma pessoa:")
nome = target = normalize('NFKD', nome).encode('ASCII','ignore').decode('ASCII')
nome = nome.lower()

if "maria" in nome or "jose" in nome:
    print ("O nome digitado possui o prenome", nome)
else:
    print ("O nome digitado não possui o prenome Maria ou José")