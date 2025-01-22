import csv
import os
import numpy as np
import matplotlib.pyplot as plt

def load_simulation_data(file_path):
    """Loads simulation data from a CSV file."""
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return [int(row[1]) for row in reader]

def compute_statistics(data):
    """Computes basic statistics for the given data."""
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std_dev": np.std(data),
        "max": np.max(data),
        "min": np.min(data)
    }

def generate_histogram(data, output_path):
    """Generates and saves a histogram of the data."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.hist(data, bins=range(1, max(data) + 1, 50), edgecolor='black')
    plt.title("St. Petersburg Game Payouts")
    plt.xlabel("Payout")
    plt.ylabel("Frequency")
    plt.yscale("log")  # Log scale for better visualization
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    INPUT_FILE = "outputs/st_petersburg_simulation.csv"
    OUTPUT_DIR = "outputs/"
    HISTOGRAM_FILE = os.path.join(OUTPUT_DIR, "payout_histogram.png")
    STATS_FILE = os.path.join(OUTPUT_DIR, "statistics.txt")

    data = load_simulation_data(INPUT_FILE)
    stats = compute_statistics(data)

    # Save statistics to a text file
    with open(STATS_FILE, 'w') as file:
        for key, value in stats.items():
            file.write(f"{key.capitalize()}: {value}\n")

    # Generate and save a histogram
    generate_histogram(data, HISTOGRAM_FILE)