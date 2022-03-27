# Heranca simples há apenas uma única classe que herda de outra classe. 
class Veiculo: # Classe Pai
    def setMaxVelocidade(self, velocidade):
        self.maxVelocidade = velocidade
        print("Velocidade Maxima definida", self.maxVelocidade)
        
class Carro(Veiculo): # Classe Filha
    def abrirPorta(self):
        print("Porta esta aberta agora. ")

hb20 = Carro()  # criando um objeto da classe Carro
hb20.setMaxVelocidade(220) # acessando métodos da classe pai
hb20.abrirPorta() # acessando o método de sua própria classe