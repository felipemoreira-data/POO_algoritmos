class Livro:

    def __init__(self, titulo,pagina, final):
        self.titulo = titulo
        self.pagina = pagina
        self.final = final


    def avancar_pagina(self, qtd_paginas) -> str:
        n = 0

        while n < qtd_paginas:
            if self.pagina < self.final:
                self.pagina += 1
                n += 1
            else:
                break
        if self.pagina == self.final:
            return f'Página final atingida --> {self.final}, você andou {n} páginas'    
                    
        return (f'Página atual do livro {self.titulo} -> {self.pagina} / após passar {qtd_paginas} páginas'
                f' Faltam {self.final - self.pagina} páginas para a conclusão do livro')
               

l1 = Livro('Pequeno principe', 20, 120)
mensagem = l1.avancar_pagina(40)
print(mensagem)