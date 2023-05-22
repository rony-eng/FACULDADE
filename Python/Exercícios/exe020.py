# implementar um programa Python para criar uma classe Veiculo
# com atributos de instância "velocidade máxima" e "quilometros percorridos por litro"

class Veiculo: #classe veiculo (pai)
    def __unit__(self, nome, velocidade_max, quilometro_litro): # atributos de classe
        self.nome = nome # atribuições da classe
        self.velcidade_max = velocidade_max # atribuições de classe
        self.quilometro_litro = quilometro_litro # atribuições de classe
    
    def capacidade_assentos(self, capacidade): #método, capacidade é um parâmetro do método, e não o atributo da classe
        print(f'A capacidade máxima de assentos do veiculo {self.nome} é {capacidade}')

    def toStr(self): # método
        print(f'nome = {self.nome}')
        print(f'velocidade máxima = {self.velcidade_max}')
        print(f'quilometro percorrido por litro = {self.quilometro_litro}')

#modelo_carro = Veiculo('fusca', 180, 10)
#modelo_carro.toStr()

# ex1: crie uma classe filha "Ônibus" que herdará todas as variáveis e 
# métodos da classe "Veiculo"

class Onibus(Veiculo):
    def capacidade_assentos(self, capacidade=70): #esse 70 já definindo a quantidade de capacidade
        return super().capacidade_assentos(capacidade=70) # o super() é referente a classe pai, chamando a classe Veiculo
                                                       # e .capacidade_assentos é chamando o método capacidade_assentos, onde chama o print.

onibus_escolar = Onibus('Scania', 120, 8)
onibus_escolar.toStr()

# ex2: modificar a classe filha "Ônibus", de modo que ela forneça a
# quantidade de assentos. Além disso, o valor desse paarâmetro deve ser 70

