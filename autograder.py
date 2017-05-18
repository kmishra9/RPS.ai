from starter_RPS import * 
#from agents import *
import agents
import Simulator
import History


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
    
    #"One test I definitely want to do for agents is creating a smart strategy that specifically can trash a reflexive_strategy that ALWAYS picks a move "
    if choice == "1":

        always_rock = biased_strategy(1, 0)
        always_paper = biased_strategy(1, 1)
        always_scissors = biased_strategy(1, 2)
        
        
        assert simulator(rock_strategy, always_rock, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return rock" 
        assert simulator(paper_strategy, always_paper, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return paper"
        assert simulator(scissors_strategy, always_scissors, simulation_count = 1000, silent = True) == (0, 0, 1), "Simulation Failed: biased_strategy(1, 0) does not always return scissors"
        
        never_rock = biased_strategy(0, 0)
        never_paper = biased_strategy(0, 1)
        never_scissors = biased_strategy(0, 2)
        
        never_rock_results = [never_rock for i in range(1000)]
        never_paper_results = [never_paper for i in range(1000)]
        never_scissors_results = [never_scissors for i in range(1000)]

        assert 0 not in never_rock_results, "Error: Invalid value generation for biased_strategy(0, 0)"
        assert 1 not in never_paper_results, "Error: Invalid value generation for biased_strategy(0, 1)"
        assert 2 not in never_scissors_results, "Error: Invalid value generation for biased_strategy(0, 2)"
        print("Passed all tests -- Step 1 complete")

    if choice == "2":
        
        simple = triple_biased_strategy(1/3, 1/3, 1/3)
        simple_test = simulator(simple_strategy, simple, simulation_count= 100000, silent = True)
        assert simple_test[0] >= 0.32 and simple_test[0] <= 0.34 and simple_test[1] >= 0.32 and simple_test[1] <= 0.34 and simple_test[2] >= 0.32 and simple_test[2] <= 0.34, "Error"

        chance = [i / 1000 for i in range(1000)]
        #Maybe make a function to do this to efficiently assign paper_chance and scissors_chance to i?
        for i in chance:
            rock_chance = i
            paper_chance = round((1 - i) / 2, 3)
            scissors_chance = paper_chance
            strat = triple_biased_strategy(rock_chance, paper_chance, scissors_chance)
            results = [strat() for _ in range(1000)]
            rock_results = len([i for i in results if i == 0])
            paper_results = len([i for i in results if i == 1])
            scissors_results = len([i for i in results if i == 2])
            assert rock_results / len(results) >= rock_chance - 0.01 or rock_results / len(results) <= rock_chance + 0.01, "Check when you're returning rock"
            assert paper_results / len(results) >= paper_chance - 0.01 or paper_results / len(results) <= paper_chance + 0.01, "Check when you're returning paper"
            assert scissors_results / len(results) >= scissors_chance - 0.01 or scissors_results / len(results) <= scissors_chance + 0.01, "Check when you're returing scissors"
            #Try to incorporate History object
        print("Passed all tests -- Step 2 complete")
    
    
    if choice == "3":
        strat = deterministic_strategy()
        deterministic_order = [0, 1, 2, 1, 0]
        simple_test_results = []
        for _ in range(len(deterministic_order)):
            simple_test_results.append(strat())
        assert simple_test_results == deterministic_order, "Failed simple test"

        for _ in range(10000):
            random_test_results = []
            strategy = deterministic_strategy()
            turns = random.randint(1, 1000)
            for _ in range(turns):
                random_test_results.append(strategy())
            answer = deterministic_order * (turns // len(deterministic_order))
            for i in range(turns - len(answer)):
                answer.append(deterministic_order[i])

            assert answer == random_test_results, "Error"
        print("Passed all tests -- Step 3 complete")
    
    if choice == "4":
        for _ in range(2):
            #rates = np.random.random(3)
            #rates /= rates.sum()
            rates = (.1, .1, .8)
            
            strategy1 = agents.triple_biased_strategy(rates[0], rates[1], rates[2])
            strategy2 = agents.reflexive_strategy
            
            agents.history = History.History(strategy1, strategy2)
            
            print(Simulator.simulator(strategy1, strategy2, history_storage = agents.history, simulation_count = 5, silent = True))
            break
            #Print statements to properly design a test
        
        print("Passed all tests -- Step 4 complete")

            
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
    
    
    
    
    
    