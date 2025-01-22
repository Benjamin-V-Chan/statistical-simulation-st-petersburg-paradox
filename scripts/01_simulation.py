# Pseudocode for 01_simulation.py
# Purpose: Simulate the St. Petersburg game multiple times and save results.

# Import necessary libraries
# Define a function to simulate one round of the St. Petersburg game:
    # Initialize payout and number of flips
    # Loop until heads is flipped:
        # Double the payout
        # Increment the flip count
    # Return the payout

# Define a function to simulate multiple games:
    # Accept the number of games as input
    # Initialize a list to store results
    # Loop for the number of games:
        # Simulate a game and append the result to the list
    # Return the list of payouts

# Define a function to save results to a CSV file:
    # Accept results and output path as inputs
    # Write results to the file

# Main script logic:
    # Set the number of simulations and output file path
    # Simulate multiple games
    # Save results to a CSV file
