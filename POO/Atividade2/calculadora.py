class Calculadora:
    def __init__(self,num1,num2):
        self.__num1 = num1
        self.__num2 = num2

    def somar(self):
        print(f"A soma dos numeros é: {self.__num1 + self.__num2}")

    def subtrair (self):
        print (f"A subtração dos nuemros é: {self.__num1 - self.__num2}")

    def multiplicar (self):
        print(f"A multipliacação dos numros é: {self.__num1 * self.__num2}")

    def dividir (self):
        if self.__num2 <= 0:
            print("Não é possíovel fazer a divisão")
        else:
            print(f"A divisão dos numeros é: {self.__num1 / self.__num2}")
        
