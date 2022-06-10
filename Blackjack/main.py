############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
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
                print("You lose")
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
                print("You win")
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