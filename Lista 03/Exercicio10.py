nota1, nota2, nota3, mediaExercicios = input("Digite a sequência as três notas e a média dos exercícios, separados por espaço: ").split(" ")
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
mediaExercicios = float(mediaExercicios)

mediaFinal= nota1+(nota2*2)+(nota3*3)+ mediaExercicios
conceito = " "

if mediaFinal>=9:
    conceito="A"
if mediaFinal>=7.5 and mediaFinal<9.0:
    conceito="B"
if mediaFinal>=6 and mediaFinal<7.5:
    conceito="C"
if mediaFinal<6:
    conceito="D"
print("Conceito final na disciplina:",conceito)