import random
# options we are taking in tuples 
options = ("rock", "paper" , "scissors")
#game should be continue for at least 3 times
playing = True
while playing:
        
    # to store the players choice 
    player = None

    # computer is giong to pick random choice from options

    computer = random.choice(options)

    #we are using while loop in order to valid input
    while player  not in options :
        player = input("Enter a choice (rock , paper , scissor):")
    #choice of player and computer
    print(f"Player: {player}")
    print(f"Copmuter: {computer}")
    # if both have the same choice 
    if player == computer:
        print("it's a tie!")

    elif  player == "rock" and computer == "scissors":
        print("You win!")

    elif player== "paper" and computer == "rock":
        print("You win!")
        
    elif player == "scissors" and computer =="paper":
        print("You win!" )    

    else :
        print("You lose!")
    #it's for player to choose whether   play again or not   
    play_again= input ("Play again? (y/n):  ").lower()  
    if not play_again == 'y':
        playing = False 

print("Thanks for Playing! ")
