# Quando uma classe é derivada de mais de uma classe base, 
# ou seja, quando uma classe possui mais de uma classe pai imediata, 
# ela é chamada de herança múltipla.

# Motor Hibrido é um motor elétrico. 
# Motor Hibrido também é um motor de combustão.

class MotorConbustao():  
    def setCapacidadeTanque(self, capacidadeTanque):
        self.capacidadeTanque = capacidadeTanque


class MotorEletrico():  
    def setCapacidadeCarga(self, capacodadeCarga):
        self.capacodadeCarga = capacodadeCarga

# Classe filha herdada de Motor a Combustao e Motor Eletrico
class MotorHibrido(MotorConbustao, MotorEletrico):
    def printDetalhes(self):
        print("Tank Capacity:", self.capacidadeTanque)
        print("Charge Capacity:", self.capacodadeCarga)

car = MotorHibrido()
car.setCapacidadeCarga("250 W")
car.setCapacidadeTanque("20 Litros")
car.printDetalhes()