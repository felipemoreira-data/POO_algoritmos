from rich import print
from rich.panel import Panel

caixa = Panel(f'Soma -> {2} + {2} = {2 + 2}', title = 'Calculadora', style= 'bold blue')
print(caixa)

def leiaInt(msg):
    while True:
        try: 
            numero = int(input(msg))
        except (TypeError, ValueError) as e:
            print(Panel(f'ERRO: {e}', title= 'ERROR', style= 'bold red'))
            continue
        except (KeyboardInterrupt) as e:
            print(Panel(f'ERRO: {e}', title= 'ERROR', style= 'bold red'))
            continue
        else:
            return numero

leiaInt('Digite o número: ')