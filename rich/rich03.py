from rich import print
from rich.table import Table
from rich.panel import Panel


tabela = Table(title = 'Tabela de Alunos')

tabela.add_column('Nome')
tabela.add_column('Idade')
tabela.add_column('Turma')

tabela.add_row('felipe', '19', '4 Semestre')


print(Panel(tabela))


