students = [
    {"id": 101, "name": "joshua", "age": 20},
    {"id": 102, "name": "samuel", "age": 21},
    {"id": 103, "name": "alex", "age": 19}
]

print("All Students:")

for student in students:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print()

search_id = int(input("Enter student ID to search: "))

found = False

for student in students:
    if student["id"] == search_id:
        print("\nStudent Found:")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        found = True
        break

if not found:
    print("Student not found.")