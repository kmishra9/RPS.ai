
from starter_RPS import * 


def test_RPS():
    return None

def test_Agents():
    prompt = "Please input which Step you'd like to test (0 through 5)"
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
        assert simulator(rock_strategy(), paper_strategy(), simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert simulator(paper_strategy(), rock_strategy(), simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        assert simulator(scissors_strategy(), rock_strategy(), simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert simulator(rock_strategy(), scissors_strategy(), simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        assert simulator(paper_strategy(), scissors_strategy(), simulation_count=1000, silent=True) == (0, 1, 0), "Simulation failed. Error in strategies"
        assert simulator(scissors_strategy(), paper_strategy(), simulation_count=1000, silent=True) == (1, 0, 0), "Simulation failed. Error in strategies"
        
        
        
    return None
    
    "One test I definitely want to do for agents is creating a smart strategy that specifically can trash a reflexive_strategy that ALWAYS picks a move "

"""
These are old tests -- we're going to need a full revamp, although obviously these 

def tests_rps():
    print("Testing...");

    msg = "Which option would you like to test?\n";
    msg += "0\t\tQuit\n";
    msg += "1\t\tdetermine_winner\n";
    msg += "2\t\tai_player\n";
    msg += "3\t\tplay_again\n";

    while True:

        print(msg);

        #Gets the key pressed
        key = utils.get_key_press();

        ###########################################
        #Quit case ('0')
        if key == 48:
            quit();
        elif key == 49:
            assert s.determine_winner("test", "rock", "rock") == "Tie, no one wins!", "Your tie statement is not correct."
            assert s.determine_winner("test", "rock", "scissors") == "test wins!", "Your user winning statement for rock > scissors is not correct."
            assert s.determine_winner("test", "scissors", "paper") == "test wins!", "Your user winning statement for scissors > paper is not correct."
            assert s.determine_winner("test", "paper", "rock") == "test wins!", "Your user winning statement for paper > rock is not correct."
            assert s.determine_winner("test", "scissors", "rock") == "AI Player wins!", "Your AI winning statement for rock > scissors is not correct."
            assert s.determine_winner("test", "rock", "paper") == "AI Player wins!", "Your AI winning statement for paper > rock is not correct."
            assert s.determine_winner("test", "paper", "scissors") == "AI Player wins!", "Your AI winning statement for scissors > paper is not correct."
            print("Tests passed.\n")
        elif key == 50:
            assert s.ai_player() in ["rock", "paper", "scissors"], "Your AI player is not returning a valid move."
            print("Tests passed.\n")
        elif key == 51:
            assert s.play_again("yes") == True, "Play again is not returning True for yes."
            assert s.play_again("no") == False, "Play again is not returning False for no."
            print("Tests passed.\n")
        else:
            print("Test does not exist for this key. ")
"""          
            
if __name__ == "__main__":
    
    prompt = "Type the number of the testing suite would you like to use: \n\t1) RPS\n\t2) AI Agents"
    test_suite = input( prompt )
    
    if test_suite == '1':
        test_RPS()
    elif test_suite == '2':
        test_Agents()
    else:
        error_msg = "Error, the testing suite you specified is not valid -- please run again and select 1 to test RPS or 2 to test AI Agents"
        print(error_msg)
    
    
    
    
    
    