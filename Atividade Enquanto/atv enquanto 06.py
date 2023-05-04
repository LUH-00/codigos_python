import os # importando biblioteca para trabalhsr com sistema operacional 
dentroIntervalo = 0 
foraIntervalo = 0
contador = 1 

os.system("cls")
while contador <= 5:
    valor = int(input(f"Informe o valor {contador}: "))
    if valor >= 10 and valor <= 20: 
        dentroIntervalo += 1 
    else: 
        foraIntervalo += 1
    contador += 1
    
os.system("cls")
print(f"Valores dentro do intervalo : {dentroIntervalo}")
print(f"Valores dentro do intervalo : {foraIntervalo}")
