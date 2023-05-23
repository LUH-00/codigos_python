from funcionario import Funcionario

f1 = Funcionario("Cleito", "Baxeador")

print(f"Seu nome é {f1.getNome()}")
f1.setNome("Isabela")
print(f"Seu nome é {f1.getNome()}")


print(f"Seu cargo é {f1.cargo}")

f1.cargo = "Gerente"

print(f"Seu cargo é {f1.cargo}")