import pandas as pd
import matplotlib.pyplot as plt

# Load employee data
employees = pd.read_csv("employees.csv")

# Display employee data
print("Employee Data:")
print(employees)

# Calculate average salary
average_salary = employees["salary"].mean()

# Find highest salary
highest_salary = employees["salary"].max()

# Display results
print("\nAverage Salary:", average_salary)
print("Highest Salary:", highest_salary)

# Create salary chart
plt.bar(employees["name"], employees["salary"])

# Add title and labels
plt.title("Employee Salaries")
plt.xlabel("Employee Name")
plt.ylabel("Salary")

# Display chart
plt.show()