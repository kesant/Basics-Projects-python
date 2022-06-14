
import data
import art
import random as np
from os import system


def jugadores ():
    terminador=True
    while terminador:
        comparador_1=np.choice(data.data)
        comparador_2=np.choice(data.data)
        if comparador_1!=comparador_2 :
            terminador=False
    comparador_1=list(comparador_1.values())
    comparador_2=list(comparador_2.values())
    return comparador_1,comparador_2
def shows_info(persona1,persona2):
    print(f"Compare A: {persona1[0]}, a {persona1[2]}, from {persona1[3]}.")
    print(art.vs)
    print(f"Against B: {persona2[0]}, a {persona2[2]}, from {persona2[3]}.")
def choose_winner(jugador_1,jugador_2,choice):
    if choice=="a" and jugador_1[1]>jugador_2[1]:
        return True,1
    elif choice=="b" and jugador_1[1]<jugador_2[1]:
        return True,2
    else :
        return False,0

    

def main(score=0,jugador="a"):
    player1,player2=jugadores()
    if jugador!="a":
        player1=jugador
    shows_info(player1,player2)
    terminador=True
    while terminador:
        player_choice=input("Who has more followers? Type 'A' or 'B': ").lower()
        game_winner,ganador=choose_winner(player1,player2,player_choice)
        if game_winner==True:
            system("cls")
            print(art.logo) 
            score+=1
            print(f"You're right! Current score:{score}")
            if ganador==1:
                main(score,player2)
            else:
                main(score,player1)
        else :
            system("cls")
            print(art.logo) 
            print(f"Sorry, that's wrong. Final score: {score}")
            terminador=game_winner
            exit()
print(art.logo)
main()


