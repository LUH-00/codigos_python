class Funcionario:
    def __init__(self, nome, cargo):
        self.__nome = nome
        self.__cargo = cargo
    
    def getNome(self):
        return self.__nome
    
    def setNome (self, valor):
        self.__nome = valor


    #CEIANDO O GET DO CARGO
    @property # esse elemento ira criar um get mais amigável
    def cargo(self):
        return self.__cargo
     
    @cargo.setter # essa forma ira criar um set para cargo mais amigavel
    def cargo(self, info):
        self.__cargo = info
    
