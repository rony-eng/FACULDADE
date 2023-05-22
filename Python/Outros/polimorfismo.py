# exemplo de polimorfismo
class Argentina():
    def capital(self):
        print('Buenos Aires é a capital da Argentina.')
    def lingua_oficial(self):
        print('O espanhol é a lingua oficial da Argentina')

class Brasil():
    def capital(self):
        print('Brasilia é a capital do Brasil')
    def lingua_oficial(self):
        print('O português é a lingua oficial do Brasil')

obj_arg = Argentina()
obj_bra = Brasil()
for pais in (obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()
# a variavel pais está se comportando de forma distinta.


# mais um exemplo de polimorfismo
class Veiculo:
    def rodar(self):
        print('Reduz o consumo de combustível')

class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print('Esse veiculo utiliza eletricidade')

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()


# exemplo de Exceção
x = 10 # regra de negócio
if x > 5: # podemos usar para manter uma margem segura para o programa, ultrapassando, alertamos ao usuário
    raise Exception('x não pode ser maior do que 5. O valor de x foi de: {}'.format(x))
