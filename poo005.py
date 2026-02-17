class Conta:

    def __init__(self,saldo):
        self.saldo = saldo

conta1 = Conta(1000)
conta1.saldo = -5000
print(conta1.saldo)
        