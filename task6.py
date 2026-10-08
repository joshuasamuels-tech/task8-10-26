class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print()


# Create two employee objects
employee1 = Employee("joshua", 21, 30000)
employee2 = Employee("rexii", 21, 40000)

# Display employee details
employee1.display_details()
employee2.display_details()