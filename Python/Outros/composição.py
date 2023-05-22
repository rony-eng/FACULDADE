class Extrato:
    def __init__(self):
        self.transacoes = []
    def imprimir(self):
        for p in self.transacoes:
            print(p[0], p[1])

class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()
    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(['DEPOSITO', valor])
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor])
            return True
class Cliente:
    def __init__(self, cpf, nome, endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        
c1 = Cliente('111111111-11', 'Ana', 'Rua das Marrecas')
c2 = Cliente('222222222-22', 'Carlos', 'Rua dos Gansos')

conta = Conta([c1,c2],24237891,2500.00)

conta.depositar(1000)
conta.sacar(500)
conta.extrato.imprimir()