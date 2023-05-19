"""
2.	Crie um dicionário que represente um grupo de pessoas e seus respectivos telefones.
 As chaves devem ser os nomes das pessoas e os valores devem ser os seus números de telefone.
   Crie uma lista com 7 contatos e em seguida, imprima a lista contendo os dicionários
"""
import os
nomes = list()
telefone = dict()

os.system ("cls")
for contador in range (0,7):
    nome = input("Informe o nome: ")
    telefone[nome]= int(input(f"informe o numero do telefone de {nome} "))
    
    nomes.append(telefone.copy())

print(nomes)
