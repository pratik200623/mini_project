subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = []  # will collect all marks in order

for sub in subjects:
    m = int(input(f"Enter {sub} marks: "))
    marks.append(m)

total = sum(marks)
percentage = (total / (len(subjects) * 100)) * 100  # out of 500 → len(subjects)*100

# grade logic
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# pass/fail: fail if ANY subject < 35
if any(m < 35 for m in marks):
    result = "Fail (one or more subjects below 35)"
else:
    result = "Pass"

# print neatly
print("\n------ Report Card ------")
print(f"Name:       {input('Enter your name: ')}")
for sub, m in zip(subjects, marks):
    print(f"{sub:<11} {m}")
print("-------------------------")
print(f"Total:      {total} / {len(subjects)*100}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade:      {grade}")
print(f"Result:     {result}")
