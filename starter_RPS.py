"""
Project: "Rock, Paper, Scissors!"

Developed by: Kunal Mishra and Jesse Luo 

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
    ~Calibrated at well below the difficulty level of UC Berkeley's 61A project, Hog and somewhat below Project 1, "2048 in Python!"

Abstraction Reference Guide:
"""

#End of first section
############################################################################################################
################################## DO NOT CHANGE ANYTHING ABOVE THIS LINE ##################################    - Section 2 -
############################################################################################################

#Start of Step 0 ###########################################################################################

def main():
    
    #Get the user's name
    name = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"
    
    continue_playing = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

    while continue_playing:
        
        play(name)
        
        continue_playing = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"

#End of Step 0 #############################################################################################



#Start of Step 1 ###########################################################################################

def get_name():
    #Write out the prompt the user will see asking them to give the program their name
    prompt = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"
    
    #Actually use a function to get the user's name
    name = ">>>>>>>>>>YOUR CODE HERE X<<<<<<<<<<"
    
    #Return the name we "got" back to where this function was called
    return name 

#End of Step 1 #############################################################################################



#Start of Step 2 ###########################################################################################

def play(name):
    """
    Modifications: changed print win to return win
    """
    
    
    print("You have 3 choices, Rock, Paper, or Scissors.")
    move = input("Enter your choice (rock, paper, scissors): ")
    
    move = move.lower()
    
    ai_move = ai_player()
    
    print(name + " plays " + move)
    print("AI plays " + ai_move)
    
    win = determine_winner(name, move, ai_move)
    
    return win

#End of Step 2 #############################################################################################











