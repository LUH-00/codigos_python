import os
pessoa = dict()
grupo = list()

grupo.append ({"nome": "João", "idade": 56})
grupo.append ({"nome": "Maria", "idade": 27})
grupo.append ({"nome": "José", "idade": 32})

os.system("cls")
print(grupo)

"""
for contador in range(0,3):
    pessoa["nome"] = input("Qual seu nome: ")
    pessoa["idade"] = int(input("Qual sua idade: "))

    grupo.append(pessoa.copy()) # criando copias do dicionário, sem criar vinculo(copiando e limpando)

print(grupo)
"""

#acessando itens do dicionário



for contador  in range(0,3):
    print(f"{grupo[contador]['nome']}: {grupo[contador]['idade']}")

#outra forma de acessar dicionario 
for linha in grupo:
    for chave, valor in linha.items():
        print(f"{chave} -- {valor}")


