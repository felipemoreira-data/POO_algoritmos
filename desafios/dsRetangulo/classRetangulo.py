class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._altura = None
        self._base = None
        self._area = None
        self.base = base
        self.altura = altura

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, float) and not isinstance(altura, int):
            raise ValueError('Tipo do valor fornecido é incorreto!')
        if altura < 0:
            raise ValueError('Valor deve ser um número positivo!')
        else:
            self._altura = altura    

    
    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance (base, float) and not isinstance (base, int):
            raise ValueError('Tipo do valor fornecido é incorreto!')
        if base < 0:
            raise ValueError('Valor deve ser um número positivo!')
        else:
            self._base = base

    @property
    def area(self):
        self._area = self.base * self.altura
        return self._area

    @area.setter
    def area(self):
        raise PermissionError('Você não pode atribuir um valor a área dessa forma!')

    @property
    def medidas(self):
        return f'Base : {self.base} \n Altura : {self.altura} \n Área : {self.area}'

    @medidas.setter
    def medidas(self, medidas: tuple):
        if not isinstance(medidas, tuple):
            raise TypeError('Valor informado deve ser uma tupla!')
        if len(medidas) != 2:
            raise SyntaxError('Dois valores (base/altura) devem ser informados!')

        if isinstance(medidas[0], float) or isinstance(medidas[0], int):
            self.base = medidas[0]
        else:
            raise TypeError('Valor informado deve ser numérico!')
        if isinstance(medidas[1], float) or isinstance(medidas[1], int):
            self.altura = medidas[1]
        else:
            raise TypeError('Valor informado deve ser numérico!')

        
        
