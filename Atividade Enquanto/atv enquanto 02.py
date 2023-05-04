"""
2. Escrever um algoritmo que leia um conjunto de números inteiros e determine o maior deles. 
A leitura do valor 0 (zero) indica o final de dados (flag).

"""

maior = 0 
while True: 
    numero = int(input("Informe um valor: "))
    if numero >=  maior: 
        maior = numero 
    if numero == 0:
        break

print(f"O maior valor dogitado foi {maior}\n")
    