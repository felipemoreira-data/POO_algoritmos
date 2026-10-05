class Diario:
    def __init__(self, senha_mestra = 'Cl#2'):
        self.__segredos = ['Sou lésbica', 'Gosto de anime', 'Não gosto da Ana']
        self.__senha = senha_mestra.strip()


    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg)
        else:
            raise ValueError(f'Erro no formato da mensagem!')

    def ler(self, senha_mestra = None):
        if isinstance(senha_mestra, str) and self.__senha == senha_mestra:
            for i, segredo in enumerate(self.__segredos):
                print(f'{i}. {segredo}')
        else:
            raise ValueError('Senha incorreta!')

    @property
    def senha(self):
        raise PermissionError('Ninguém tem acesso a senha!')

    @senha.setter
    def senha(self, dados):
        if not isinstance(dados, (tuple, list)) or len(dados) != 2:
            raise ValueError('Autenticação fracassada, senha incorreta!')

        senha_atual, nova_senha = dados

        if senha_atual == self.__senha:
            self.__senha = str(nova_senha).strip()
            
        else:
            raise ValueError('Senha incorreta!')        

