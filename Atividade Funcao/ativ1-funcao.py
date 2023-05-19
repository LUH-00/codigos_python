
idade = int(input("informe a idade do aluno: "))

def informar (i):
    if idade >=5 and idade <= 7:
        return ("INFANTIL A")
    
    if idade >=8 and idade <=10:
        return ("INFANTIL B")
    
    if idade >= 11  and idade <= 13:
        return ("JUVENIL A")
    
    if idade >= 14 and idade <= 17:
        return ("JUVENAL B")
  
    if idade >= 18:
        return("ADULTO")

print(f"{informar(idade)}")