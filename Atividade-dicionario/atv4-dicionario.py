"""
4.	Crie um dicionário que represente uma playlist de músicas. 
As chaves devem ser os nomes das músicas e os valores devem ser as informações adicionais (como o nome do artista ou tempo de duração).
 Crie uma lista com 7 itens e ao final exiba o conteúdo da lista

"""
import os
playlist = list()
musica = dict()

os.system ("cls")
for contador in range(2):
    nome = input("Qual o nome da musica: ")
    artista = input("Qual o nome do artista: ")
    tempo = float(input("Qual a duração da musica?: "))

    musica[nome] = {"Artista": artista, "Duração": tempo}
    
    playlist.append(musica.copy())
    musica.clear()

print(playlist)

