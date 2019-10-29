from random import*

lista = []

while len(lista)<10:
    lista.append(randint(0,100))

print(lista)

int1 = int(input("Digite um numero inteiro: "))
int2 = int(input("Digite outro numero inteiro: "))

naoEsquerda = True
naoDireita = True

for numero in lista:
    if numero == int1 or numero==int2:
        esquerda = numero
        print("Valor achado primeiro pela esquerda: ", esquerda)
        naoEsquerda = False
        break
   

listaReversa = lista[:]
listaReversa.reverse()

for numero in listaReversa:
    if numero == int1 or numero==int2:
        direita = numero
        print("Valor achado primeiro pela direita: ", direita)
        naoDireita = False
        break

if naoDireita == True and naoEsquerda == True:
    print ("O valor não foi encontrado em nenhuma da listas")


