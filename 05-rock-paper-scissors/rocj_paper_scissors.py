
# Play rock, paper, scissors against the computer until you quit.

import random
BEARS ={"rock" : "scissors" , "paper" :"rock" , "scissors" : "paper"}

def result (player, computer):
    if player == computer:
        return "Tie!"
    if BEATS[player] == computer:
        return "You Win!"
    return "You lose!"

def main():
    while True:
        player = input("rock , paper, scissors (or Quirt): " ).lower().strip()
        if player == "quit":
            break
        if player not in BEATS:
            print("Invalid choice.")
            continue
        computer = random.choice (list(BEATS))
        print(f"Computer cose {computer}.{result(player, computer)}")

if __name__ == "__main__":
    main()