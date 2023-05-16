lista = ["João ", 30 , "Cohab"]

pessoa = {            #dicionario 
    "nome":"Maria",
    "idade":24,
    "bairro": "Renascença"
}

print(lista[0])
print(pessoa, "\n") 

# exibindo as chaves  utilizando o comando keys ()
print (pessoa.keys(), "\n")

#exibindo os valores utilizando o comando values()
print(pessoa.values(), "\n")

#exibindo os tanto a chave como o valor utilizando o comando items()
print(pessoa.items(), "\n")

#Exibindo 
for chave, valor in pessoa.items():
    print (f"{chave} : {valor}")
