from hashlib import sha256

class ContaBancaria:
    '''
    Essa classe cria e define uma conta bancária para os clientes!
    '''
    def __init__(self, id: int,nome: str, saldo: float = 0, senha: str = None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if senha is None:
            senha = self.pedir_senha()
        self.__hash = sha256(senha.encode('utf-8')).hexdigest()
 

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novo_nome:str, senha:str = None):
        if senha is None:
            senha = self.pedir_senha()
        if self.validar_senha(senha):
            if len(novo_nome) >= 3:
                self._titular = novo_nome    

    def __str__(self):
        return f'Final: titular {self.nome} possui R${self.__saldo:,.2f} de saldo na conta!'

    def validar_senha(self, senha):
        usuario = sha256(senha.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def pedir_senha(self):
        from pwinput import pwinput
        while True:
            senha = str(pwinput('Senha: '))
            if len(senha) >= 6:
                break
        return senha    


    def depositar(self, deposito):
        self.__saldo += deposito
        print(f'Depósito de R${deposito:,.2f} na conta {self._id}')

    def sacar(self, saque:float, senha:str = None):
        saque = abs(saque)
        if senha is None:
            senha = self.pedir_senha()
        if self.validar_senha(senha):
            if saque > self.__saldo:
                print(f'SALDO INSUFICIENTE PARA SACAR R${saque:,.2f} NA CONTA {self._id}')
            else:
                self.__saldo -= saque    
                print(f'Saque de R${saque:,.2f} na conta {self._id}')
        else:
            print('Senha inválida!')        