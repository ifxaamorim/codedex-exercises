class ContaBancaria:
    def __init__(self,primeiro_nome, segundo_nome,id_conta, tipo_de_conta,pin,saldo):
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.id_conta = id_conta
        self.tipo_de_conta = tipo_de_conta
        self.pin = pin 
        self.saldo = saldo

    def desposito(self, valor):
        self.saldo += valor
        return self.saldo
    
    def saque(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def display_saque(self):
        print(f"Seu saldo atual é: {self.saldo} usd")


pedro = ContaBancaria("Pedro", "Amaral", 23, "Conta corrente", 123, 100)

pedro.desposito(96)
pedro.display_saque()
pedro.saque(100)
pedro.display_saque()