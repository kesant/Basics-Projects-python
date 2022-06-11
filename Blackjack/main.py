import art 
import random as rd
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def status(list_player,list_computer):
    print(f"Your cards: {list_player}, current score: {sum(list_player)}" )
    print(f"Computer's first card: {list_computer[0]}")
def convertidor_de_as(lista):
    """converst the as into 1 if the score is greater than 21"""
    if sum(lista)>21 and (11 in lista):
        indice=lista.index(11)
        lista[indice]=1

def another_try(player_card,computer_card):
    ending_game2=True
    while ending_game2:
        status(player_card,computer_card)
        new_try=input(f"Type 'y' to get another card, type 'n' to pass:").lower()
        
        if new_try=="y":
            if sum(player_card)>21:
                  
                print(f"Your final hand: {player_card}, final score: {sum(player_card)}" )
                print(f"Computer's final hand:{computer_card}, final score: {sum(computer_card)}")
                print("You lose the game")
                start_game()
            else :
                player_card.append(rd.choice(cards))
                convertidor_de_as(player_card)
                if sum(computer_card)<17:
                    computer_card.append(rd.choice(cards))
                    convertidor_de_as(computer_card)
                
                        
        else :
            status(player_card,computer_card)
            print(f"Your final hand: {player_card}, final score: {sum(player_card)}" )
            print(f"Computer's final hand:{computer_card}, final score: {sum(computer_card)}")
            if sum(player_card)<=21 and  sum(player_card)>sum(computer_card):
                print("You win the game")
                start_game()
            else :
                print("You lose")
                start_game()
        
def start_game():
    entry =input("Do you want to play a game of Blackjack? Type 'y' or 'n' :").lower()
    end_game=True
    while end_game :
        if entry=="y":
            computer_card=[]
            player_card=[]
            for pos in range(2):
                player_card.append(rd.choice(cards))
                computer_card.append(rd.choice(cards))
            
            another_try(player_card,computer_card)
        else:
            end_game=False
            exit()

start_game()
