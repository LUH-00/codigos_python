""" 
4. A fábrica de refrigerantes Mega-Refri vende seu produto em três formatos: lata de 350 ml, garrafa de 600 ml e garrafa de 2 litros. 
Um comerciante deseja comprar os três tipos de produtos. 
Faça um algoritmo que leia a quantidade de refrigerante em lata, a quantidade de refrigerante de 600ml e a quantidade de refrigerante de 2 litros. 
Ao final mostre a quantidade de litros de refrigerante que o comerciante comprou.

"""
print ("Fabrica Mega - Refri")

lata = int(input("Informe a quantidade de lata 350ml "))
garrafa =int(input("Informe a quantidae de garrafa 600ml "))
garrafa2l = int(input("Informe a quantidade de garrafa de 2l "))

soma = (350 * lata) + (600 * garrafa) + (2000 * garrafa2l)

print(f"A soma de as compras em ml são {soma}")