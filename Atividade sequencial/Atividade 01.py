"""
1. Faça um algoritmo que leia a idade de uma pessoa expressa em anos e mostre-a expressa em  meses e dias. 

"""
idade = int(input("Informe a sua idade"))
meses =  (idade) * 12
dias = (idade)* 365

print (f"Você tem {idade} anos {meses} meses e {dias} dias")