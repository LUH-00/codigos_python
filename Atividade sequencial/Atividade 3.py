"""
3. Faça um algoritmo que leia do usuário o nome da fazenda e a quantidade de cavalos que vivem nessa fazenda. 
Ao final deverá ser calculada a quantidade de ferraduras necessárias para equipar todos os cavalos. 
Deverá ser mostrado algo como:

"""
fazenda = input ("Informe o nome da fazenda ")
print ("O nome da fazenda é ", fazenda)

cavalos = int(input("Informe a quantidade de cavalos "))
ferraduras = (cavalos) * 4

print (f"A fazenda {fazenda} tem {cavalos} cavalos e todos os cavalos precisão de {ferraduras} ferraduras")