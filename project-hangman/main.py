from dis import dis
import random as rd
import list_words
import hangman_ascii

print(hangman_ascii.logo)
print(f"{'*'*15}WELCOME TO HANGMAN GAME{'*'*15}")
stages=hangman_ascii.stages
display=[]
chosen_word=rd.choice(list_words.word_list)

for i in range(len(chosen_word)):
    display.append("_")

end_game=True
lives=6
while end_game and lives!=0:

    guess=input("Guess a letter: ").lower()
    if guess in chosen_word:
        if guess in display:
            print(f"You've already guessed the letter {guess}")
        else:
            for letter in range(len(chosen_word)):   
                if guess==chosen_word[letter]:
                    display[letter]=guess
    else:
        print("you guessed the wrong letter , you lose a life")
        lives-=1
    print(f"{' '.join(display)}")    
    print(stages[lives])
    if "_" not in display:
        print("You win")
    if lives==0:
        print("Game over")        
