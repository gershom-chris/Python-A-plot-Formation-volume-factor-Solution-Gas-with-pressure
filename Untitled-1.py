import pandas as pd
import matplotlib.pyplot as plt

data = {
    'pressure': [3600, 3200, 2800, 2500, 2400, 1800, 1200, 600, 200],  # Added two more pressure values
    'solutiongas': [567, 567, 567, 567, 554, 436, 337, 223, 143],
    'formation-volume-factor': [1.31, 1.317, 1.325, 1.333, 1.31, 1.263, 1.21, 1.14, 1.07]
}

# Create a DataFrame
dataset = pd.DataFrame(data)

# Creating axes object and defining the plot
ax = dataset.plot(kind='line', x='pressure', y='solutiongas', color='blue', linewidth=3)
ax2 = dataset.plot(kind='line', x='pressure', y='formation-volume-factor', secondary_y=True, color='red', linewidth=3, ax=ax)

# Title of the plot
plt.title("FVF VS Rs")

# Labeling x and y-axes
ax.set_xlabel('pressure', color='g')
ax.set_ylabel('solutiongas', color="b")
ax2.set_ylabel('formation-volume-factor', color='r')

# Defining display layout
plt.tight_layout()

# Show the plot
plt.show()
