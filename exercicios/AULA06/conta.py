class ContaCorrente:

    def __init__(self, nome_cliente, num_conta, senha, saldo = 0.0):
        self.nome_cliente = nome_cliente
        self.num_conta = num_conta
        #self.agencia = agencia
        self.senha = senha
        #self.cartao_credito = cartao_credito
        #self.financiamento = financiamento
        #self.cheque_especial = cheque_especial
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'O saldo de {self.nome_cliente} disponível é {self.saldo:.2f}')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque realizado com sucesso.\nNovo saldo é {self.saldo:.2f}.')
        else:
            print('Saldo insuficiente!')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito realizado com sucesso.\nNovo saldo é {self.saldo:.2f}.')
        else:
            print('Não pode depositar valores negativos.')

    def transferir(self, valor, destinatario):
        if self.num_conta != destinatario.num_conta:
            ContaCorrente.sacar(self, valor)
            ContaCorrente.depositar(destinatario, valor)
        else:
            print('Não pode realizar a tranferência para você mesmo.')