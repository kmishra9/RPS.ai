from starter_RPS import * 
from agents import *


def test_RPS():
    prompt = "Please input which Step you'd like to test (0 through 5)\n"
    choice = input(prompt).strip()
    name = "random name"
    
    #Test cases for Step 0
    if choice == "0":
        
        #dummy functions to help run tests
        def get_name():
            return "random name"
        
        def play(name, ai):
            return "random name"
        
        def play_again():
            print(test)
            return False
            
        assert main() == "test", "Step 0 is incorrect"
        
        print("Testing for step 0 complete")
        
    
    
    #Test cases for Step 1
    if choice == "1":
        origin_input = __builtins__.input
        __builtins__.input = lambda x: name
            
        assert get_name() == name, "Step 1 is incorrect"
        print("Testing for step 1 complete")
    
    #Test cases for Step 2
    if choice == "2":
        def determine_winner(ai_move, move, name):
            return False
        
        #check general case
        assert play(name, basic_ai) == False, "step 2 is incorrect"
        
        print("Testing for step 2 complete")
    
    #Test cases for Step 3
    if choice == "3":
       
        origin_input = __builtins__.input
        __builtins__.input = lambda x: "yes"
        assert play_again() == True, "step 3 is incorrect"
        
        
        origin_input = __builtins__.input
        __builtins__.input = lambda x: "no"
        assert play_again() == False, "step 3 is incorrect"
        
        print("Testing for step 3 complete")
    
    #Test cases for Step 4
    if choice == "4":
        assert basic_ai() == ("rock" or "paper" or "scissors"), "step 4 is incorrect"
        
        print("Testing for step 4 complete")
    #Test cases for Step 5
    if choice == "5":
        assert determine_winner("random player", "rock", "rock") == "Tie, no one wins!"
        assert determine_winner("random player", "rock", "paper") == "You lose!", "You should lose in this case"
        assert determine_winner("random player", "scissors", "rock") == "You lose!", "You should lose in this case"
        assert determine_winner("random player", "paper", "scissors") == "You lose!", "You should lose in this case"
        assert determine_winner("random player", "paper", "rock") == "random player wins!", "You should win in this case"
        assert determine_winner("random player", "rock", "scissors") == "random player wins!", "You should win in this case"
        assert determine_winner("random player", "paper", "scissors") == "random player wins!", "You should win in this case"
        print("Testing for step 3 complete")
        
    return None   
        

def test_Agents():
    prompt = "Please input which Step you'd like to test (0 through 5)\n"
    choice = input(prompt).strip()
    
    #Test cases for Step 0
    if choice == "0":
        
        #Testing general output
        for i in range(1000):
            assert 0 == rock_strategy(), "rock_strategy is incorrect"
            assert 1 == paper_strategy(), "paper_strategy is incorrect"
            assert 2 == scissors_strategy(), "scissors_strategy is incorrect"
            assert 0 <= simple_strategy() <= 2, "simple_strategy is incorrect"
            
        #Testing simulator runs
        assert simulator(rock_strategy, paper_strategy, simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert simulator(paper_strategy, rock_strategy, simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        assert simulator(scissors_strategy, rock_strategy, simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert simulator(rock_strategy, scissors_strategy, simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        assert simulator(paper_strategy, scissors_strategy, simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert simulator(scissors_strategy, paper_strategy, simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        assert (simulator(rock_strategy, rock_strategy,          simulation_count=1000, silent=True) == 
               simulator(paper_strategy, paper_strategy,        simulation_count=1000, silent=True) ==
               simulator(scissors_strategy, scissors_strategy,  simulation_count=1000, silent=True) == 
               (0, 0, 1)), "Simulation failed -- when run against each other, the strategies did not completely tie"
               
        #Simple strategy should always win 1/3, lose 1/3, and tie 1/3 -- no matter the complexity of its opponent
        sr = [round(x, 2) for x in simulator(simple_strategy, rock_strategy,       silent=True)]
        sp = [round(x, 2) for x in simulator(simple_strategy, paper_strategy,      silent=True)]
        ss = [round(x, 2) for x in simulator(simple_strategy, scissors_strategy,   silent=True)]
        assert sr == sp == ss and sr[0] == sr[1] == sr[2] == .33, "Simulation failed. Error in strategies"
        
        print("Passed all tests -- Step 0 complete")

        
    return None
    
    "One test I definitely want to do for agents is creating a smart strategy that specifically can trash a reflexive_strategy that ALWAYS picks a move "

            
if __name__ == "__main__":
    
    prompt = "Type the number of the testing suite would you like to use: \n\t1) RPS\n\t2) AI Agents\n"
    test_suite = input( prompt )
    
    if test_suite == '1':
        test_RPS()
    elif test_suite == '2':
        test_Agents()
    else:
        error_msg = "Error, the testing suite you specified is not valid -- please run again and select 1 to test RPS or 2 to test AI Agents"
        print(error_msg)
    
    
    
    
    
    