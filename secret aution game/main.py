from os import system
import art
def chose_winner(dictionary):
    names=[]
    bids=[]
    for name in dictionary:
        names.append(name)
        bids.append(dictionary[name])
    indice=bids.index(max(bids))
    print(f"the winner is {names[indice]} with a bid of ${bids[indice]}")
print('WELCOME TO THE SECRET AUCTION GAME  ')
print(art.logo)
print('WANNA MAKE A BET ?')
ending_game=False
dic_bid={}
while ending_game==False:
    nombre=input("what is your name ? : ")
    bet=int(input("what is your bid ? : $"))
    dic_bid[nombre]=bet
    controller=input("Are there any other biders ? type 'Yes' or 'No' :").lower()
    if controller=="no":
        ending_game=True
    system("cls")
chose_winner(dic_bid)
