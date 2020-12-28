class Aritmetica:
    """Clase Artimetica para realizar las operaciones de sumar, restar, etc"""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self):
        """Se realiza la operación con los atributos de la clase"""
        return self.operando1 + self.operando2   
    
    def restar(self):
        return self.operando1 - self.operando2   
    
    def multiplicar(self):
        return self.operando1 * self.operando2   
    
    def dividir(self):
        return self.operando1 / self.operando2   
             
    
#Creamos un nuevo objeto
aritmetica = Aritmetica(2, 4)  
print("Resultado sumar:", aritmetica.sumar())  
print("Resultado restar:", aritmetica.restar())  
print("Resultado multiplicar:", aritmetica.multiplicar())  
print("Resultado dividir:", aritmetica.dividir())  

#Creamos otro objeto
aritmetica2 = Aritmetica(3, 5)  
print("Resultado sumar:", aritmetica2.sumar())  
print("Resultado restar:", aritmetica2.restar())  
print("Resultado multiplicar:", aritmetica2.multiplicar())  
print("Resultado dividir:", aritmetica2.dividir())  
