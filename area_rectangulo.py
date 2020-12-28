class Rectangulo:
    
    
    def __init__(self, base, altura ): #inicializo las variables
        self.base=base
        self.altura=altura
        
        
    def Calcular_area(self): #se crea este metodo con el fin de hacer la operacion de calculo de area
        return self.base*self.altura
    
rectangulo1=Rectangulo(5,10)  #de este modo cuando se dan los datos por defecto
print(rectangulo1.Calcular_area())
print(id(rectangulo1))


# aca cuando los datos se piden por consola

base = int(input("digite base: ")) 
altura = int(input("digite altura: "))

rectangulo2=Rectangulo(base , altura)
print(rectangulo2.Calcular_area())
print(id(rectangulo1))