"""
5. Um barril de refresco é feito com 8 partes (80%) de água mineral e 2 partes (20%) de suco de maracujá.  
Faça um algoritmo para calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco. 
A quantidade de litros de refresco deve ser informada pelo usuário

""" 
litro = int(input("Informe a quantidade de litros "))
agua = litro * 0.8
suco = litro* 0.2   

print (f"A quantidae de litos informada {litro}L, precisa de {agua}% de agua e {suco}% de suco\n\n")