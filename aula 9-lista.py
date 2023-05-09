notas = [9.5, 7.0, 6.5, 9]
print(notas)
print(type(notas))

for item in notas:
    print(item)
    
notas[2] = 8.5

print("="*30)
print(notas)

# inserindo valores na lista 
#Forma 1
notas.append(4) # colocou o elemento 4 no final da lsita 
print(notas, "\n")

print ("*"*30)
#Forma 2
notas.insert(1, 10) # insert precisa de 2 paremetros. 1 é o índice que desejo inserir o valor(posição). 2 é o valor propriamente ditp que quero inserir(valor).
print(notas,  "\n")

print("="*30)

#Removendo valores 
#Forma 1

notas.pop()#exclui o último elemento
print(notas, "\n")

print("*"*30)

#Forma 2
notas.pop (2) # removendo pelo indice(posiçao)
print(notas, "\n")

print("*"*30)

#Forme 3
notas.remove(9.5)# o remove() exclie usando o conteúdo da lista como parâmetro
print(notas, "\n")








