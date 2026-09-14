name = input("Enter student name: ")
mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))

total_mark = mark1 + mark2
avg_mark = total_mark / 2
result = "Pass" if avg_mark >= 50 else "Fail"

print(f"Student Name: {name}")
print(f"Total Mark: {int(total_mark) if total_mark.is_integer() else total_mark}")
print(f"Average Mark: {int(avg_mark) if avg_mark.is_integer() else avg_mark}")
print(f"Result: {result}")