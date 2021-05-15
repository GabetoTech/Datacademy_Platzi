
def winner(player1, player2):
    if player1 == "piedra":
        if player2 == "piedra":
                return ('Empate')
        elif player2 == "papel":
                return ('jugador 2')
        elif player2 == "tijera":
                return ('jugador 1')
        else:
            print("Adios")
    if player1 == "papel":
        if player2 == "piedra":
                return ('jugador 1')
        elif player2 == "papel":
                return ('Empate2')
        elif player2 == "tijera":
                return ('jugador 2')
    if player1 == "tijera":
        if player2 == "piedra":
                return ('jugador 2')
        elif player2 == "papel":
                return ('jugador 1')
        elif player2 == "tijera":
                return ('Empate')
                  

if __name__ == "__main__":
    
    print("Bienvenido al juego de piedra, papel o tijera, esta versión es para dos jugadores")
    player1 = str(input('Jugador 1, escoja entre piedra, papel o tijera:  '))
    player2 = str(input('Jugador 2, escoja entre piedra, papel o tijera:  '))
    finalwin= winner(player1, player2)
    print(f'El ganador de esta partida es el {winner(player1, player2)}')