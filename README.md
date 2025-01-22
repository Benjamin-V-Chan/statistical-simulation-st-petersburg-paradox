# statistical-simulation-st-petersburg-paradox

## Project Overview

The St. Petersburg Paradox is a famous concept in probability theory and decision theory that highlights the contrast between expected value and practical decision-making. The paradox involves a hypothetical game of chance where a fair coin is flipped repeatedly until it lands on heads. The payoff for the game is 2^n, where n is the number of flips required to get heads. Despite the infinite expected value of this game, most individuals are unwilling to pay large amounts to play it, creating a paradox.

### Mathematical Explanation

The expected value (EV) of the St. Petersburg game is calculated as follows:

EV = sum (from n = 1 to infinity) of (1 / 2^n) * (2^n)

Where:

(1 / 2^n): The probability of obtaining heads on the nth flip.

(2^n): The payout if heads is obtained on the nth flip.

Simplifying this:

EV = sum (from n = 1 to infinity) of 1 = infinity.

This infinite expected value creates a theoretical paradox when compared to human behavior, where individuals typically assign a much lower value to the game.

This project simulates the paradox using Python to analyze the payouts over multiple games and provides statistical insights into the results.

## Folder Structure

```
project-root/
├── scripts/
│   ├── 01_simulation.py       # Script to simulate the St. Petersburg game
│   ├── 02_analysis.py         # Script to analyze simulation results
├── outputs/
│   ├── st_petersburg_simulation.csv  # Simulation results
│   ├── payout_histogram.png          # Histogram of payouts
│   ├── statistics.txt                # Basic statistical analysis
├── requirements.txt          # List of Python dependencies
├── README.md                 # Project documentation
```

## Usage

### 1. Setup the Project:

- Clone the repository.
- Ensure you have Python installed.
- Install required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 2. Run the Simulation:

Use the following command to simulate the St. Petersburg game:

```bash
python scripts/01_simulation.py
```

This will generate a CSV file with the simulation results in the `outputs/` folder.

### 3. Analyze the Results:

To perform statistical analysis and generate a histogram of the results, run:

```bash
python scripts/02_analysis.py
```

This will create:
- `statistics.txt`: A text file with basic statistics.
- `payout_histogram.png`: A histogram of the payouts.

## Requirements

- Python 3.8 or higher
- Required Python libraries (install using requirements.txt):
  - matplotlib
  - numpy
  - csv

## Conclusion

This project offers a hands-on way to explore the St. Petersburg Paradox by simulating the game, analyzing outcomes, and understanding its implications on probability theory and decision-making. Customize the scripts to conduct additional experiments or extend the analysis further.