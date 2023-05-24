import os
from pessoa import Pessoa, Aluno, Professor

os.system ("cls")
p1 = Pessoa("Carla", 23)
a1 = Aluno("Jose", 40)
a2 = Professor ("Ruan", 35)

p1.relatorio()
a1.relatorio()
a1.mostraAluno()
a2.relatorio()

a2.mostraProfessor()