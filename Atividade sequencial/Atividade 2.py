"""
2. Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em horas e mostre-o expresso em minutos e segundos. 

"""
fabrica = "Luan e cia"
print ("O nome da fabrica é: ",fabrica)

tempo = int(input("Informe quanto tempo você trabalhou na fabrica " ))
minutos = (tempo) * 60
segundos = (tempo)* 3600
print (f"Você trabalhou {tempo} horas, {minutos} minutos e {segundos} segundos")