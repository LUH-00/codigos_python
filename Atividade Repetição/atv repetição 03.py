"""
•	Escreva um algoritmo , que leia um conjunto de 6 fichas, cada uma contendo, a altura e o código do sexo de uma pessoa 
(código = 1 se for masculino e 2 se for feminino), e calcule e imprima: 
- a maior e a menor altura da turma; 
- a média de altura das mulheres;
- a média de altura da turma.

"""
mediaTurma = 0
mediaMulheres = 0
maior = 0
somaTurma = 0
somaMulheres = 0
contMulheres = 0



for contador in range(1,7):
    altura = float(input("Informe a sua altura"))
    sexo = int(input("Informe o código do sexo: 1-masc ou 2-fem: "))

    if contador == 1:
        menor = altura 
    else:
        if altura >= maior:
            maior = altura

        if altura <= menor:
            menor = altura
            
    if sexo == 2:
        somaMulheres += altura
        contMulheres += 1

        somaTurma += altura

print(f"A maior altura é {maior} e a menor altura é {menor}")
print(f"A média de alturras das mulheres é {somaMulheres / contMulheres}")
print(f"A média de altura das turmas é {somaTurma / 6}\n")

