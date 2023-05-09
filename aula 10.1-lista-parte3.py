#import random
from random import randint
import os

os.system("cls")
sorteio = [] # criando uma lista vazia

for contador in range (1,11):
    sorteio.append(randint(1,100))  # gerando valores aleatórios e salvando na lista 

# valor = randint(1,100) # essa função irá gerar um numero aleatório entre 1 e 100
print(sorteio)
sorteio.sort(reverse= True) # a funçáo sort( )ordena de forma crescente. O  parametro reverse=True, faz de forma decrecente 
print(sorteio)
os.system("Pause")# irá pausar o sistema até uma tecla ser pressionada  