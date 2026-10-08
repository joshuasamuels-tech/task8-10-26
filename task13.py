import numpy as np

# Create a NumPy array containing marks
marks = np.array([75, 85, 90, 68, 95, 82, 78, 88])

# Calculate mean, maximum and minimum
mean_mark = np.mean(marks)
maximum_mark = np.max(marks)
minimum_mark = np.min(marks)

# Find marks greater than 80
above_80 = marks[marks > 80]

# Display the results
print("Marks:", marks)
print("Mean Mark:", mean_mark)
print("Maximum Mark:", maximum_mark)
print("Minimum Mark:", minimum_mark)
print("Marks greater than 80:", above_80)