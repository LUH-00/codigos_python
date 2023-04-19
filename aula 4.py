print ("******* Título *******")
texto = "técnico em desenvolvimento de sistemas"
print (texto)

idade = int(input("Informe a sua idade "))
print ( "*"* idade) # o "*"*20 calcula a quantidade de *

# manipulando textos (String)


# contar a quantidade de caractere 
print ("O total de letras é ", len (texto)) # lEN vem de lengt, que significa total

 # deixar todo texto maiusculo | minusculo  
print(texto.upper()) # upper coloca todo texto em maiusculo | LOWER coloca todo texto em minusculo

print(texto.capitalize()) # coloca a 1º letra em maiusculo

# coloca o texto no lugar de outo
print (texto.replace("sistemas", "web")) # replase troca um texto por outro

# TRABALHANDO COM FATIAMENTO

print ("Fatiando a variavel texto")
print(texto[:3]) # vai exibir todo o texto até a posição 2, no caso a posição 3 não conta.

print(texto[3:]) # vai exibir todo o textoo a partir da posção 3

print(texto[3:10]) # Vai exibir todo o texto que está na posição 3 até 10