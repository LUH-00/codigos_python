salario = float(input("Informe seu salaio: "))
financiamento = float(input("Qual o valor do financiamento: "))

valor5x = financiamento * 5 

if valor5x <= salario:
    print("Financiamento concedido\n")
else: 
    print("Financimanto não concedido\n")

print("Obrigado por nos consultar\n")