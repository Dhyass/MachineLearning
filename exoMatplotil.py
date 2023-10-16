# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:04:47 2023

@author: NONZOOU
"""

"""
    Vous avez un dictionnaierr qiui comprend N datasetes.
    creer une fonction qui trace N graphiques sur une seule figure
    
    Indication : exemple pour 4 eperience
    
    dataset = {f"experience{i}": np.random.randn(100) for i in range(4) }
        ## crere une fonction graphique qui va tracer les resultas des ces experiences sur une meme figure
        
"""
import numpy as np
import matplotlib.pyplot as plt

def plot_experiments(dataset):
    # Create a figure to hold the subplots
    plt.figure(figsize=(10, 6))

    # Iterate through the experiments and create a subplot for each
    for i, (experiment_name, data) in enumerate(dataset.items(), 1):
        plt.subplot(3, 2, i)  # Assuming 4 experiments, adjust as needed
        plt.plot(data)
        plt.title(experiment_name)
    
    # Adjust the layout to prevent overlapping titles
    plt.tight_layout()

# Create a sample dataset with 4 experiments
dataset = {f"experience{i} By NONZOOU": np.random.randn(100) for i in range(1, 7)}

# Call the function to plot the experiments
plot_experiments(dataset)

# Display the figure
plt.show()
