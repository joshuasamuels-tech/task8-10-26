import pandas as pd

# Create students.csv file
data = {
    "name": ["joshua", "rexii", "alex", "pysone", "benedict"],
    "age": [20, 21, 19, 20, 22],
    "mark": [85, 92, 78, 88, 75]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

# Load the CSV file using Pandas
students = pd.read_csv("students.csv")

# Display the first 5 rows
print("First 5 rows:")
print(students.head())

# Calculate average mark
average_mark = students["mark"].mean()
print("\nAverage Mark:", average_mark)

# Display students who scored above 80
print("\nStudents who scored above 80:")
print(students[students["mark"] > 80])