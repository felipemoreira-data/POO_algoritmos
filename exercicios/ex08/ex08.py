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
        self._titular = nome ## Protected (#)
        self.__saldo = saldo ## Private (-)

    def __str__(self):
        return f'Final: titular {self._titular} possui R${self.__saldo:,.2f} de saldo na conta!'

    def depositar(self, deposito):
        deposito = abs(deposito)
        self.__saldo += deposito
        texto(f'Depósito de R${deposito:,.2f} na conta {self.id}')

    def sacar(self, saque):
        saque = abs(saque)
        if saque > self.__saldo:
            texto(f'SALDO INSUFICIENTE PARA SACAR R${saque:,.2f} NA CONTA {self.id}')
        else:
            self.__saldo -= saque    
            texto(f'Saque de R${saque:,.2f} na conta {self.id}')


