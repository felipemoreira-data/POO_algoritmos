from classFrete import Transporte, Moto, Caminhao, Drone
from rich import print

def main():
    while True:
        transporte = str(input('Qual o meio de transporte que gostaria do seu frete? /' \
        '[Moto/Caminhão/Drone]')).strip().lower()
        distancia = int(input('Distância a ser percorrida: '))

        if transporte not in ('moto', 'drone', 'caminhão'):
            print ('Inválido')
            continue
        if transporte == 'moto':
            transporte = Moto(distancia, None)
            frete_t = transporte.calc_frete()
            print(f'[bold blue]Frete Calculado com a motocicleta -->[/bold blue] [bold green]R${frete_t:,.2f}[/bold green]')
            break



    t1 = Moto(2_000, None)
    frete_t1 = t1.calc_frete()
    print(f'[bold blue]Frete Calculado com a motocicleta -->[/bold blue] [bold green]R${frete_t1:,.2f}[/bold green]')

    t2 = Caminhao(51_000, None)
    frete_t2 = t2.calc_frete()
    if not frete_t2:
        print('Impossível realizar o transporte de caminhão nessa distância!')
    else:
        print(f'[bold blue]Frete Calculado com o caminhão -->[/bold blue] [bold green]R${frete_t2:,.2f}[/bold green]')


    t3 = Drone(12_000, None)
    frete_t3 = t3.calc_frete()
    if not frete_t3:
        print('Impossível realizar o transporte com o drone nessa distância!')
    else:
        print(f'[bold blue]Frete Calculado como drone -->[/bold blue] [bold green]R${frete_t3:,.2f}[/bold green]')


if __name__ == '__main__':
    main()