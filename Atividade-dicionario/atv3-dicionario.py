"""
3.Crie um dicionário que represente uma tabela de preços de um restaurante. 
 As chaves devem ser os nomes dos pratos e os valores devem ser os preços correspondentes.
 Você pode criar uma lista contendo 8 valores. Ao final mostre a lista

"""

import os

produtos = list()
preço = dict()

os.system("cls")
for contador in range (1,3):
    nome = input("Informe o nome do prato desejado: ")
    preço [nome] = int(input(f"Informe o preço da(o) {nome}: "))

    produtos.append(preço.copy())

print (produtos)