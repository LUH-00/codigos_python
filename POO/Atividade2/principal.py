import os
from calculadora import Calculadora
os.system ("cls")

num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))

exibir = Calculadora (num1, num2)

exibir.somar()
exibir.subtrair()
exibir.multiplicar()
exibir.dividir()