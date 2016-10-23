"""
Project: "RPS.ai"

Developed by: Kunal Mishra 

Inspired by: http://www.nytimes.com/interactive/science/rock-paper-scissors.html?_r=0

Developed for: Beginning students in Computer Science

To run: python3 agents.py

Student Learning Outcomes:
    Various levels of comfort with:
        small projects and abstraction
        understanding and modeling off existing code
        variables
        functional programming
        loops and conditionals
        randomness, probability, distributions
        APIs
        Modulus Theory
        AI Reflex agents
        
Skill Level:
    Assumed knowledge of language and concepts, but without mastery of them. Some comfort with language syntax and concepts is assumed at this point, however, and strong critical thinking and abstraction skills are necessary.
    ~20+ hours of experience/class/lecture coming into this project
    ~Calibrated at around the same difficulty level of the "strategies" portion of UC Berkeley's 61A project, Hog and slightly above Project 1, "2048 in Python!"


Abstraction Reference Guide:

	Simulator - A simulator takes in two strategies, an optional history object, and an optional simulation_count. 
        Note: A history argument does NOT need to be passed in unless the strategy requires it. simulation_count does not need to be changed from the default unless an instructor specifies (you can ignore it).
        Note: Examples showing how to use the simulator are found in the Simulator.py file
        
	History - A History object takes in two strategies and keeps track of the history of those two strategies playing against each other in a Simulator 
        
        get_chronological_history()
            Gets the history of moves by both strategies in chronological order (will not be able to tell which history is which)
        
    
        get_opponent_chronological_history(own_strategy)
            Gets the history of moves by the opponent, in chronological order
            Arg own_strategy: the strategy that you're calling this from (used to determine the opponent)
    
    
        get_opponent_frequency(own_strategy)
            Given which strategy is calling to get the opponent's move frequency, the function returns the opponent's move frequency
            Arg own_strategy: the function that is called within the simulator (used to determine the opponent)
            Returns a tuple of frequencies in the format of (rock_frequency, paper_frequency, scissor_frequency)
            
    Agents - AI strategy functions that return between 0 and 2, inclusive
        
        always_rock_strategy - always returns 0 (rock)
        always_paper_strategy - always returns 1 (paper)
        always_scissors_strategy - always returns 2 (scissors)
        
        simple_strategy - returns all moves with equal weight from 0, 1, 2 (rock, paper, scissors)
        
        biased_strategy - has a single weighted move, equal split for other two
        triple_biased_strategy - has a weight for each move
        
        deterministic_strategy - repeats a pattern of moves
        
        reflexive_strategy - Keeps track of all past opponent moves and adjusts weights/probability of playing each move 
        predictive_strategy - Attempts to predict what the user will play next, given its last move
        reflexive_and_predictive_strategy - an optimal strategy that takes in a number N and keeps track of the sequence of past user moves of length N. Searches through all past history for sequences of length N to predict what the next move will be and counter it
"""

from Simulator import *
from History import *
import random
history = None

def opposite_move(move):
    #Returns a move that defeats the incoming move argument

    #Returns Paper if move is Rock
    if move == 0:
        return 1
    #Returns Scissors if move is Paper
    if move == 1:
        return 2
    #Returns Rock if move is Scissors
    if move == 2:
        return 0


##########################################################################
# DO NOT CHANGE ANYTHING ABOVE THIS LINE
##########################################################################




##########################################################################
# In this section, you'll be creating artificial intelligence agents that play RPS against each other!
# Each agent you define should always return 0 (rock), 1 (paper), or 2 (scissors)
# Three examples of the most simplistic strategies possible (always
# choosing one move, no matter what)



#Start of Step 0 ###########################################################################################

def always_rock_strategy():
    return ">>>>>>>>>>YOUR CODE HERE 0-0<<<<<<<<<<"


def always_paper_strategy():
    return ">>>>>>>>>>YOUR CODE HERE 0-1<<<<<<<<<<"


def always_scissors_strategy():
    return ">>>>>>>>>>YOUR CODE HERE 0-2<<<<<<<<<<"


def simple_strategy():
    return ">>>>>>>>>>YOUR CODE HERE 0-3<<<<<<<<<<"

#End of Step 0 #############################################################################################



#Start of Step 1 ###########################################################################################

def biased_strategy(bias, biased_move):
    """
    Arg bias: a number between 0 and 1, denoting the percentage of the time the biased_move is played
    Arg biased_move: a number between 0 and 2, inclusive, signifiying which move the strategy should be biased towards
    @Return: a function that can be called by the simulator
    """
    range_size = 100

    def generate_biased_move():
        generated = int(random.random() * range_size)
        ">>>>>>>>>>YOUR CODE HERE 1<<<<<<<<<<"
            
    
    
    
    #Returns the function that will actually do the generation but doesn't need the arguments passed in each time
    return generate_biased_move     #Do not change

#End of Step 1 #############################################################################################



#Start of Step 2 #############################################################################################

def triple_biased_strategy(rock_bias, paper_bias, scissor_bias):
    """
    Arg rock_bias: a float between 0 and 1, denoting the percentage of the time rock should be played
    Arg paper_bias: a float between 0 and 1, denoting the percentage of the time paper should be played
    Arg scissors_bias: a float between 0 and 1, denoting the percentage of the time scissors should be played
    @Return: a function that can be called by the simulator
    """
    
    range_size = 100

    def generate_biased_move():
        generated = int(random.random() * range_size)
        ">>>>>>>>>>YOUR CODE HERE 2<<<<<<<<<<"




    #Returns the function that will actually do the generation but doesn't need the arguments passed in each time
    return generate_biased_move     #Do not change

#End of Step 2 #############################################################################################



#Start of Step 3 #############################################################################################

def deterministic_strategy():
    #Plays rock, paper, scissors, paper, rock in that sequence, over and over 
    deterministic_order = [0, 1, 2, 1, 0]
    length_of_sequence = len(deterministic_order)
    
    count = 0

    def generate_deterministic_move():
        ">>>>>>>>>>YOUR CODE HERE 3<<<<<<<<<<"
    
    
    
    
    #Returns the function that will actually do the generation but doesn't need the arguments passed in each time
    return generate_deterministic_move      #Do not change

#End of Step 3 #############################################################################################



#Start of Step 4 #############################################################################################

def reflexive_strategy():
    # Allows strategies to utilize the history while simulating the strategies
    # against each other
    # rock: 0, paper;1, scissors: 2
    rock_freq, paper_freq, scissor_freq = history.get_opponent_frequency( reflexive_strategy )

    ">>>>>>>>>>YOUR CODE HERE 4<<<<<<<<<<"

#End of Step 4 #############################################################################################



#Start of Step 5 #############################################################################################

def predictive_strategy():
    opp_history = history.get_opponent_chronological_history( predictive_strategy )
    size_history = len(opp_history)
    
    ">>>>>>>>>>YOUR CODE HERE 5<<<<<<<<<<"

#End of Step 5 #############################################################################################


############################################################################################################
######################## Optional Challenge -- ATTEMPT AFTER FINISHING PROJECT #############################
############################################################################################################

def reflexive_and_predictive_strategy():
    ">>>>>>>>>>YOUR CODE HERE 6<<<<<<<<<<"



############################################################################################################
######################## Playground - FEEL FREE TO USE DURING PROJECT ######################################
############################################################################################################

if __name__ == "__main__":
    "Play around with strategies as you feel fit -- check out the examples in Simulator.py if you need help"
