from art import logo
print(logo)

alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def game():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesar(text,shift,direction)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar (start_text,shift_amount,cipher_direction):
    new_word=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)+shift_amount
            new_word+=alphabet[position]
        else:
            new_word+=char
    print(f"The {cipher_direction} text is {new_word}") 

end_game=True
while end_game==True:
    game()
    desition=input("Do you want to keep playing ? Y/N :")
    if desition.lower()=="n":
        end_game=False
        print("Thanks for playing")