"""
4. Ler um valor N e mostrar todos os valores inteiros entre 1 (inclusive) e N (inclusive).Considerar que o N será sempre maior que ZERO.

"""
    
final = int(input("Informe um valor maior que zero: "))

contador  = 1
while contador <= final:
    print (contador, end=" ")
    contador += 1
