# Multi-level de heranca -> eh quando uma classe eh derivada de uma classe
# que é derivada de outra classe, ela eh chamada de heranca muitinivel.

# Um carro eh um veiculo e hibrido eh um carro

class Veiculo: # Classe Pai
    def setMaxVelocidade(self, velocidade):
        self.maxVelocidade = velocidade
        print("Velocidade Maxima definida", self.maxVelocidade)
        
class Carro(Veiculo): # Classe Filha de Veiculo
    def abrirPorta(self):
        print("Porta esta aberta agora. ")

class Hibrido(Carro): # Classe filha de Carro
    def ligarhibrido(self):
        print("Modo hibrido esta ligado.")
        
        
hb20_plus = Hibrido()  # criando um objeto da classe Carro
hb20_plus.setMaxVelocidade(220) # acessando métodos da classe pai
hb20_plus.abrirPorta() # acessando o método da classe pai
hb20_plus.ligarhibrido() #acessando o método da classe filha