import random
def get_choices():
    player_choice=input("Enter your choice: rock, paper or scissors: ") #takes input from the player
    options=["rock", "paper", "scissors"]
    computer_choice= random.choice(options) #randomly selects an option from the list
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def get_winner(player,computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player==computer:
        return "It's a tie!"
    elif player=="rock":
        if computer=="scissors":
            return "Player wins!"
        else:
            return "Computer wins!"
    elif player=="scissors":
        if computer=="paper":
            return "Player wins!"
        else:
            return "Computer wins!"
    elif player=="paper":
        if computer=="rock":
            return "Player wins!"
        else:
            return "Computer wins!"
    else:
        return "Invalid input! You have not entered rock, paper or scissors, try again."
   

choices = get_choices()
result = get_winner(choices["player"], choices["computer"])
print(result)






