'''name = input("Enter your name: ")  # taking name from usermaths
math = int(input("Enter your maths marks: "))  # taking maths marks from user
science = int(input("Enter your science marks: "))  # taking science marks from user
english = int(input("Enter your english marks: "))  # taking english marks from user
history = int(input("Enter your history marks: "))  # taking history marks from user
computer = int(input("Enter your computer marks: "))  # taking computer marks from user



total = math + science + english + history + computer # calculating total marks

percentage = (total/500)*100 # calculating percentage marks
if percentage >= 90:
    gread = "Grade A"
elif percentage >= 75:
    gread = "Grade B"
elif percentage >= 50:
    gread = "Grade C"
else:
    gread = "Fail"

#pass/fail logic(if any subject <35 ,student fails)
if math < 35 or science < 35 or english < 35 or history < 35 or computer < 35:
    result = "fail ( becouse one or more subject are below 35 marks)"
else:
    result= "pass"

print("------ report card ------")
print(f"Name:   {name}")  # printing name
print(f"Maths marks:   {math}")  # printing maths marks
print(f"Science marks:   {science}")  # printing science marks
print(f"English marks:   {english}")  # printing english marks
print(f"History marks:   {history}")  # printing history marks
print(f"Computer marks:   {computer}")  # printing computer marks


print("-------------------------------")
print(f"Total marks:   {total}")  # printing total marks
print(f"Average marks:   {percentage:.2f}")  # printing average marks
print(f"grade:   {gread}")  # printing grade
print(f"result:   {result}")  # printing result
'''
 
lis1 = []
for i in range(1,6):
    num = int(input(f"Enter number {i}: "))
    lis1.append(num )
print(lis1)