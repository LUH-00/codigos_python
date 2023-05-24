class Conta:
    def __init__(self, numero, titular, saldo, limite=100):
        self.__numero = numero # em python tornamos um elemento privado com 2 underlines. Com 1 underline ele está protegido. Com nenhum underline, está público.
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite # esse atriputo possui um valor padrão de forma que o usuario poderá ou não informar este valor 


    def relatorio(self):
        print(f"Olá, {self.__titular} o numero da sua conta é {self.__numero} e o seu saldo atual é R${self.__saldo} e o seu limite é R${self.__limite}")
     
    def exibirSaldo (self):
        print (f"O seu saldo é {self.__saldo}")

    # O método GET irá retornar ou exibir o valor do atributo
    def getLimite(self): 
        return self.__limite
    
    #O método SET irá alterar o conteúdo do atributo, sem exibir nada
    def setLimite(self, valor):
    

        if valor < 0:
            print("Valor menor que zero, infome outro valor")
        else:
            self.__limite = valor

    #vamos modificar o atributo saldo com @peoperty e @ssetter

    @property
    def saldo(self):
        print(f"Olá, seu saldo é {self.__saldo}\n")


    @saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            print("Você não pode inserir valor negativo ou zero \n")
        else:
            self.__saldo = valor