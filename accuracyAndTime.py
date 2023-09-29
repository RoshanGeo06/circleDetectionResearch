import matplotlib.pyplot as plt

# Model names
models = ['Model 1', 'Model 2', 'Model 3', 'Model 4', 'Model 5']

# Time taken for each model (replace with your actual time values)
time_taken = [0.333, 0.345365, 0.6467, 0.7346745, 0.16]  # Replace these with your actual time values

# Create a bar graph
plt.bar(models, time_taken, color='skyblue')

# Adding labels and title
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Accuracyfor 5 Models')

# Display the graph
plt.show()
