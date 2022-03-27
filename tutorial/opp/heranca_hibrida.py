# Um tipo de herança que é uma combinação de herança múltipla e multinível 
# é chamada de herança híbrida.

# Motor a combustao é um motor. 
# Motor Eletrico é um motor. 
# Motor Hibrido é um motor elétrico e um motor de combustão.

class Motor:  # Classe Pai
    def setPotencia(self, potencia):
        self.potencia = potencia


class MotorCombustao(Motor):  # Classe filha herdada do Engine
    def setCapacidadeTanque(self, capacidadeTanque):
        self.capacidadeTanque = capacidadeTanque


class MotorEletrico(Motor):  # Classe filha herdada do Engine
    def setCapacidadeCarga(self, capacidadeCarga):
        self.capacidadeCarga = capacidadeCarga

# Classe filha herdada de Motor combustao e Motor eletrico


class MotorHibrido(MotorCombustao, MotorEletrico):
    def printDetalhes(self):
        print("Potencia:", self.potencia)
        print("Capacidade do Tanque:", self.capacidadeTanque)
        print("Capacidade da Carga:", self.capacidadeCarga)


car = MotorHibrido()
car.setPotencia("2000 CC")
car.setCapacidadeCarga("250 W")
car.setCapacidadeTanque("20 Litros")
car.printDetalhes()