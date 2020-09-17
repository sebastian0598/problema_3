import os 
class cliente():
    os.system('cls')
    def __init__(self,nombre):
        self.nombre = nombre
        self.cantidad = 0
    def depositar_cantidad(self,cantidad):
        self.cantidad += cantidad
    def extraer_cantidad(self,cantidad):
        self.cantidad -= cantidad
    def devolver_cantidad(self):
        return self.cantidad
    def imprimir(self):
        print(f"el cliente {self.nombre} tiene depositado en total: {self.cantidad}")  
def main():
    



    

if __name__ == "__main__":
    main()