"""
Project: "Rock, Paper, Scissors!"

Developed by: Kunal Mishra, Jesse Luo, and Jamie Delbick 

Developed for: Beginning students in Computer Science

To run: python3 starter_RPS.py

Student Learning Outcomes:
    Various levels of comfort with:
        small projects and abstraction
        understanding and modeling off existing code
        variables and lists
        functional programming
        loops and conditionals
        input/output
        artificial intelligence agents

Skill Level:
    assumed knowledge of language and concepts, but without mastery or even comfortability with them
    ~3-6 hours of experience/class/lecture necessary, coming into this project (for RPS) and 25-35 hours (for the AI extensions)
    ~Calibrated at well below the difficulty level of UC Berkeley's 61A project, Hog and somewhat below "2048 in Python!"

Abstraction Reference Guide:
"""

#End of first section
############################################################################################################
################################## DO NOT CHANGE ANYTHING ABOVE THIS LINE ##################################    - Section 2 -
############################################################################################################

#Start of Step 0 ###########################################################################################

def main():
    
    #Get the user's name
    name = get_name()
    
    continue_playing = True

    while continue_playing:
        
        play(name)
        
        continue_playing = play_again()

#End of Step 0 #############################################################################################



#Start of Step 1 ###########################################################################################

def get_name():
    
    #Write out the prompt the user will see asking them to give the program their name
    prompt = "Enter your name: "
    
    #Use a function to get the user's name (using the prompt)
    name = input( prompt )
    
    #Return the name we "got" back to where this function was called
    return name 

#End of Step 1 #############################################################################################



#Start of Step 2 ###########################################################################################

def play(name, ai=basic_ai, silent=False):
    
    #Write out the prompt the user will see asking them to give the program their choice
    prompt = "Enter your choice: "
    
    #Use a function to get the user's move (using the prompt)
    move = input( prompt )
    
    #Ensure the move is formatted properly (all lowercase letters)
    move = move.lower()
    
    #Get the AI's move
    ai_move = ai()
    
    #Use a functional abstraction to figure out who won -- the user or the AI
    winner = determine_winner(ai_move, move)
    
    #Check if the function is supposed to be silent or not -- print only if silent is False
    if (silent == False):
        print(name + " plays " + move)
        print("AI plays " + ai_move)
        print(winner + " wins!")
    
    return winner

#End of Step 2 #############################################################################################



#Start of Step 3 ###########################################################################################

def play_again():
    
    #Write out the prompt the user will see asking them whether they want to play again or not
    prompt = "Do you want to play again? (Yes or No)" 
    
    #Use a function to get the user's choice (using the prompt)
    choice = input( prompt )
    
    #Ensure the choice string is formatted properly (all lowercase letters)
    choice = choice.lower()
    
    #If the choice was _____, the user wants to play again
    if (choice == "yes"):
        return True
    
    #If the choice was _____, the user does not want to play again
    elif (choice == "no"):
        return False
    
    #If the choice was anything else, it wasn't valid input
    else:
        print("Invalid input!\n")
        return play_again()
        #Introduction to recursion! Ask a TA if you're curious as to how a function is calling itself!
    
#End of Step 3 #############################################################################################



#Start of Step 4 ###########################################################################################

def basic_ai():
    #The three possible moves, represented as strings
    moves = ["rock", "paper", "scissors"]
    
    #Randomly select an index from moves
    index = int(random.random() * 3)            #For the sake of teaching distributions, we use int(random.random() * n) -- and cuz its slightly more difficult and stimulating
    #Note to Jamie: I changed it from 2 to 3 because random.random() generates a number between in the range[0,1). 
    #Then, when you multiply by n (the number , you get a float in the range [0,3]. Then you typecast the float to an int and the range is then 
    
    return moves[index]

#End of Step 4 #############################################################################################



#Start of Step 5 ###########################################################################################

def determine_winner(name, move, ai_move):
    assert ( (move    == "rock" or move    == "paper" or move    == "scissors") and 
             (ai_move == "rock" or ai_move == "paper" or ai_move == "scissors")
           ), "Wrong move or ai_move argument passed in"
    
    #Tie case
    if move == ai_move:
        return "Tie, no one wins!"
    
    #Win case 1
    elif move == "rock" and ai_move == "scissors":
        return name + " wins!"
    
    #Win case 2
    elif move == "paper" and ai_move == "rock":
        return name + " wins!"
    
    #Win case 3    
    elif move == "scissors" and ai_move == "paper":
        return name + " wins!"
    
    #Losing case
    else:
        return "The computer wins!"
    

#End of Step 5 #############################################################################################




