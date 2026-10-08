# Create and write to the file
with open("students.txt", "w") as file:
    file.write("joshua - 85\n")
    file.write("alex - 92\n")
    file.write("Rexii - 78\n")

# Read and display the file contents
with open("students.txt", "r") as file:
    contents = file.read()

print("Student Details:")
print(contents)