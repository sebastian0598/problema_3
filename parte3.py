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


def main():
    banco1 = banco()
    banco1.operacion_banco()



    

if __name__ == "__main__":
    main()