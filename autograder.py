#from starter_RPS import *
from agents import *


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
        sr = map(lambda x: round(x, 2), simulator(simple_strategy, rock_strategy,       silent=True))
        sp = map(lambda x: round(x, 2), simulator(simple_strategy, paper_strategy,      silent=True))
        ss = map(lambda x: round(x, 2), simulator(simple_strategy, scissors_strategy,   silent=True))
        
        assert sr == sp == ss and sr[0] == sr[1] == sr[2], "Simulation failed. Error in strategies"
        
        print("Passed all tests -- Step 0 complete")

        
    return None
    
            
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