
import random as rd
import art
def select_dificulty():
    contador=True 
    while contador  :
        number=input("Choose a dificulty .Type 'easy' or 'hard' :").lower()
        if number != "easy" and number != "hard":
            print("you chose a wrong choice")
        else:
            contador=False
    return number
def choose_winner(number):
    player_numb=int(input("Make a guess :"))
    if player_numb==number:
        print("you win")
        exit()
    elif player_numb>number:
        print("too high")
        print("guess again")
    elif player_numb<number:
        print("too low")
        print("guess again")

def tries(dificulty,number):
    if dificulty=='easy':
        for intento in range(5):
            choose_winner(number)
    else:
        for intento in range(10):
            choose_winner(number)
print(art.logo)
print("WELCOME TO THE NUMBER GUESING GAME")
print("I'm thinking of a number between 1 and 100 ")
number_random=rd.randint(0,10)
dificulty=select_dificulty()
tries(dificulty,number_random)
    
