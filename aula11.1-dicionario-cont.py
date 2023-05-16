import os
estado = {"uf": "Maranhão", "Sigla":"MA"}

os.system("cls")
print(estado)

#inserindo dados em um dicionário
#forma 1 
estado["população"] = "20.000.000" #adicionando uma nova informação na variável 
print(estado)

#forma 2
estado.update({"capital":"São Luis"})
print (estado)

#Removendo itens do dicionario
#forma 1 
estado.pop("uf")
print(estado)


#forma 2
del(estado["população"])
print(estado)

#forma 3 - apaga todo conteúdo
estado.clear()
print(estado)