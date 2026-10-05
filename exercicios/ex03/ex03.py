import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from interface.interface import texto

class ContaBancaria:
    '''
    Essa classe cria define uma conta bancária para os clientes!
    '''
    def __init__(self, id,nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f'Final: titular {self.titular} possui R${self.saldo:,.2f} de saldo na conta!'

    def depositar(self, deposito):
        self.saldo += deposito
        texto(f'Depósito de R${deposito:,.2f} na conta {self.id}')

    def sacar(self, saque):
        if saque > self.saldo:
            texto(f'SALDO INSUFICIENTE PARA SACAR R${saque:,.2f} NA CONTA {self.id}')
        else:
            self.saldo -= saque    
            texto(f'Saque de R${saque:,.2f} na conta {self.id}')




p1 = ContaBancaria(id = 1, nome = 'Ana', saldo= 3000)
p1.depositar(300)
p1.sacar(5_000)
print(p1)