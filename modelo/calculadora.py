class Calculadora:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def get_num1(self):
        return self.num1
    
    def set_num1(self, num1):
        self.num1 = num1
    
    def get_num2(self):
        return self.num2
    
    def set_num2(self, num2):
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 == 0:
            raise ValueError("No se puede dividir entre cero")
        return self.num1 / self.num2
