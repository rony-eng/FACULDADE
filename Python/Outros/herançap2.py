import datetime
class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
# herança simples
class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor])
            return True

# herança múltipla
class Poupanca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()
    def remuneraConta(self):
        self.saldo += self.saldo * self.taxaremuneracao

# herança múltipla 2
class ContaRemuneradaPoupanca(Conta, Poupanca):
    def __init__(self, clientes, numero, saldo, taxaremuneracao):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao # nem precisa pois já está pegando de poupança
    def remuneraConta(self):
        self.saldo += self.saldo*(self.taxaremuneracao/30)

c1 = Cliente('111111111-11', 'Ana', 'Rua das Marrecas')
c2 = Cliente('222222222-22', 'Carlos', 'Rua dos Gansos')
cx = ContaRemuneradaPoupanca([c1, c2], 98939123, 1500.00, 0.03)
cx.remuneraConta()
print(cx.saldo)