lanche = ("Pizza", "Hotdog" , "Refri", "Batata")
idades = tuple (18 ,20, 12) # putra formar de criar tuplas                                                         

print (lanche)
print(type(lanche)) # estou mostrando o tipo da variavel 

print(lanche[1])
print(f"O total de lanches é {len(lanche)} \n") #  length

#lanche{2} = "Suco"

for contador in range (0, 4):
    print(lanche[contador])

print("-"*30)

for item in lanche:
    print(item)

print("-"*30)
#enumenrate serve para permitir acessar os índices da tupla. Já a variavel, ira armazenar os valores do indice
for indice,elemento in enumerate(lanche):
    print (f"{indice} = {elemento}")
