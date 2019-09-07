import numpy as np


def get_user_bet():
    while True:
        try:
            bet = input("Enter the starting bet: ")
            bet = float(bet)
        except ValueError:
            print("value must be a real number. Try again.")
        except:
            print("something unexpected occurred.")
            return None
        else:
            if bet < 0.0:
                print("You must place a positive, nonzero bet! Try again.")
            else:
                return bet

# TODO: Check for case when initial amount is largest amount won!  
def play_lucky_sevens():
    game_money = get_user_bet()
    if game_money == None:
        return None
    total_rolls = max_won = max_roll_count = 0.0
    while game_money > 0.0:
        if game_money > max_won: 
            max_won = game_money
            max_roll_count = total_rolls
        print("You currently have", game_money, "dollars")
        rolls = [np.random.randint(1,7) for i in np.arange(2)]
        print("you rolled a", rolls[0], "and a", rolls[1])
        game_money += (4. if (sum(rolls) == 7) else -1.)
        total_rolls += 1
              
    print("looks like you lost the game!")
    
    print("Results:")
    print("Total rolls before going broke:", total_rolls)
    print("Highest amount won:", max_won)
    print("Roll count at highest amount won:", max_roll_count)

np.random.seed(321)
while True:
    play_lucky_sevens()
    yes_or_no = input("Play again (y/n)? ")
    while yes_or_no.lower() not in ["y","n"]:
        print("Invalid input. Try again")
        yes_or_no = input("Play again (y/n)? ")
    if yes_or_no.lower() == "n": 
        print("Thanks for losing!")
        break  
    else:
        print("Give it one more shot, I believe in you!") 
        

