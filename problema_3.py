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

class banco(cliente): 
    def __init__(self):
        self.cliente1 = cliente(input("digite el nombre del cliente: "))
        self.cliente2 = cliente(input("digite el nombre del cliente: "))
        self.cliente3 = cliente(input("digite el nombre del cliente: "))
    def operacion_banco(self):
        self.cliente1.depositar_cantidad(int(input("digite la cantidad a depositar: ")))
        self.cliente1.extraer_cantidad(int(input("digite la cantidad a extraer: ")))
        self.cliente2.depositar_cantidad(int(input("digite la cantidad a depositar: ")))
        self.cliente2.extraer_cantidad(int(input("digite la cantidad a extraer: ")))
        self.cliente3.depositar_cantidad(int(input("digite la cantidad a depositar: ")))
        self.cliente3.extraer_cantidad(int(input("digite la cantidad a extraer: ")))
    def deposito_total(self):
        self.total =  self.cliente1.devolver_cantidad() + self.cliente2.devolver_cantidad() + self.cliente3.devolver_cantidad()
    def total_banco(self):
        print(f"el total del banco es:  {self.total}")
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
def main():
    
    banco1 = banco()
    banco1.operacion_banco()
    banco1.deposito_total()
    banco1.total_banco()



    

if __name__ == "__main__":
    main()