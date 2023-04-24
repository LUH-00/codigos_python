percurso = float(input("Informe o percurso em Km: "))
tipoCarro = int(input("Informe o tipo do carro, 1, 2 ou 3: "))

if tipoCarro == 1: #== verdade absoluta 
    total = percurso / 8
    print (f"O tipo do carro é {tipoCarro} vai precisar de {total} litros de gasolina \n")                                                   #pass  pra não coçocar conteudo
elif tipoCarro == 2:
    total= percurso / 9
    print (f"O tipo do carro é {tipoCarro} vai precisar de {total} litros de gasolina \n")
    
elif tipoCarro == 3:
    total= percurso / 12
    print (f"O tipo do carro é {tipoCarro} vai precisar de {total} litros de gasolina \n")
    

else:
    print("Tipo carro inválido \n")                      