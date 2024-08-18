import random

def jugar():
    user = input("Escoge una opcion: 'pi' piedra , 'pa' papel , 'tijera' tijera.\n").lower()
    computadora = random.choice(['pi' , 'pa' , 'ti'])
    
    if user == computadora:
        return 'Empate'

    if gano_el_jugador(user, computadora):
        return 'Ganaste'
    
    return 'Perdiste'

def gano_el_jugador(jugador, oponente):
    if((jugador == 'pi' and oponente == 'ti')
       or (jugador == 'ti' and oponente == 'pa')
       or (jugador == 'pa' and oponente == 'pi')):
       return True
    else:
        return False

print(jugar())