horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
tempo = horas*60+minutos

print("Hora atual: {0:02}:{1:02} ".format(horas, minutos))
print("Se passaram {} minutos desde o ínicio do dia. ".format(tempo))
