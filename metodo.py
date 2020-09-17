    def deposito_total(self):
        self.total =  self.cliente1.devolver_cantidad() + self.cliente2.devolver_cantidad() + self.cliente3.devolver_cantidad()
    def total_banco(self):
        print(f"el total del banco es:  {self.total}")
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()
        
def main():
    banco1.deposito_total()
    banco1.total_banco()



    

if __name__ == "__main__":
    main()