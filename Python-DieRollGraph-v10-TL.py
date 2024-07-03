################################ 
# Tom Lutzenberger 
# Python-DieRollGraph-v10.py
# Date: March 21, 2024
# Version: 1.0
# Description: A python program that randomly rolls an imaginary dice and graphs the results 
# as the rolls occur. The program continues until the designated number of rolls are completed.
################################

# import library functions to use
import random
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

# Initialize the figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
sns.set_style('whitegrid')

# Initialize empty lists to store data
rolls = []
roll_counts = [0] * 6  # Initialize with zeros for each die face
roll_percentages = []

# Function to update the plot
def update(frame):
    # Simulate rolling a six-sided die
    roll = random.randint(1, 6)
    rolls.append(roll)
    
    # Count the frequency of each roll value
    roll_counts[roll - 1] += 1
    
    # Percentage Calculation
    total_rolls = len(rolls)
    roll_percentages = [count / total_rolls * 100 if total_rolls > 0 else 0 for count in roll_counts]
    
    # Bar plot updating
    ax1.clear()
    ax1.bar(range(1, 7), roll_counts, color='skyblue')
    ax1.set_title('Die Roll Frequencies')
    ax1.set_xlabel('Roll Value')
    ax1.set_ylabel('Frequency')
    ax1.set_ylim(0, max(roll_counts) + 10)

    ax2.clear()
    ax2.bar(range(1, 7), roll_percentages, color='lightgreen')
    ax2.set_title('Die Roll Percentages')
    ax2.set_xlabel('Roll Value')
    ax2.set_ylabel('Percentage')
    ax2.set_ylim(0, 100)
    for i, p in enumerate(ax2.patches):
        ax2.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Update in real time as data change
ani = FuncAnimation(fig, update, frames=100, interval=200, repeat=False)

plt.tight_layout()
plt.show()

