
dias= int( input ("Digite uma quantidade de dias: ") )
horas= int( input ("Digite uma quantidade de horas: ") )
minutos= int( input ("Digite uma quantidade de minutos: "))
segundos = int( input ("Digite uma quantidade de segundos: ")) 

diasC= dias*86400
horasC= horas*3600
minutosC= minutos*60
total= diasC+horasC+minutosC+segundos

print("A soma de tempo lido corresponde a um total de",total,"segundos")




