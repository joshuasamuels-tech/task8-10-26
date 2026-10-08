
import json

# Read the JSON file
with open("employees.json", "r") as file:
    employees = json.load(file)

# Display each employee's name and department
print("Employee Details:")

for employee in employees:
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print()