class Pessoa:
    # atributos (Molde)
    nome = "Luan"
    idade = 20
    altura = 1.65

    #métodos
    def falar(self, texto):# self é um parâmetro obrigatório do python que informa que o método pertence à própria classe
        print(texto)

pessoa1 = Pessoa()
pessoa1.nome = "José" # mudando o valor da variável 
print(pessoa1.nome, pessoa1.idade, pessoa1.altura)

pessoa1.falar("Olá mundo")
