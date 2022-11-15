import random

print('Piedra, Papel o Tijeras'.center(50, '*'))
def juego():
    player1 = input('Opciones: \n1. Piedra \n2. Papel \n3. Tijera \nSeleccione(1-3):  ')
    player2 = random.choice(['Piedra', 'Papel', 'Tijera'])

  
    if (player1 == 'Piedra' and player2 == 'Tijera') or (player1 == 'Papel' and player2 == 'Piedra') or (player1 == 'Tijera' and player2 == 'Papel'):
        print(f'{player1} - {player2}')
        print(f' Jugador 1 - Haz Ganado')
    
    elif (player2 == 'Piedra' and player1 == 'Tijera') or (player2 == 'Papel' and player1 == 'Piedra') or (player2 == 'Tijera' and player1 == 'Papel'):
        print(f'{player2} - {player1}')
        print(f'Jugador 2 - Haz Ganado')

    else:
        print(f'{player1} - {player2}')
        print(f'EMPATE')


juego()
