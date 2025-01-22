import random
import csv
import os

def simulate_game():
    """Simulates one round of the St. Petersburg game."""
    payout = 1
    flips = 0
    while random.choice([True, False]):  # Flip until heads (True)
        payout *= 2
        flips += 1
    return payout

def simulate_multiple_games(num_games):
    """Simulates multiple rounds of the St. Petersburg game."""
    results = []
    for _ in range(num_games):
        results.append(simulate_game())
    return results

def save_results_to_csv(results, output_path):
    """Saves simulation results to a CSV file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Game", "Payout"])
        for i, payout in enumerate(results, start=1):
            writer.writerow([i, payout])

if __name__ == "__main__":
    NUM_SIMULATIONS = 10000
    OUTPUT_FILE = "outputs/st_petersburg_simulation.csv"

    results = simulate_multiple_games(NUM_SIMULATIONS)
    save_results_to_csv(results, OUTPUT_FILE)