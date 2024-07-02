import random

def display_random_literals():
    x = 0  # Counter for "Heads"
    y = 0  # Counter for "Tails"
    literals = ["Heads", "Tails"]  # List of literals
    
    for i in range(1, 4):  # Loop runs for rounds 1 to 3
        random_literal = random.choice(literals)
        
        # Count occurrences of each literal
        if random_literal == "Heads":
            x += 1
        else:
            y += 1
        
        # Display the round number and the random literal
        print(f"Round {i}: {random_literal}")
    
    print(f"Total counts - Heads: {x}, Tails: {y}")


# Call the function to start the program
display_random_literals()
