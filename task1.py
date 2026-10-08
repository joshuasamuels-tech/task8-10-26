name = input("Enter student's name: ")

mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
