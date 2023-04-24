a = float(input("Informe o lado A: "))
b = float(input("Informe o lado B: "))
c = float(input("Informe o lado C: "))

if (a < b+c )and (b < a+c) and c < a+b:
    print ("Temos um triangulo")
else:
    print ("Você não tem um triangulo \n ")