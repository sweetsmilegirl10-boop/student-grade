# Initial version of grade.py
name = input("Enter student name: ")
mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))

avg_mark = (mark1 + mark2) / 2

print(f"Student Name: {name}")
print(f"Average Mark: {avg_mark}")