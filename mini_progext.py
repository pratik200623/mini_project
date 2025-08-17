name = input("Enter your name: ")  # taking name from usermaths
math = int(input("Enter your maths marks: "))  # taking maths marks from user
science = int(input("Enter your science marks: "))  # taking science marks from user
english = int(input("Enter your english marks: "))  # taking english marks from user

total = math + science + english  # calculating total marks

averge = total / 3  # calculating average marks
 


print("------ report card ------")
print("Name:", name)  # printing name
print("Maths marks:", math)  # printing maths marks
print("Science marks:", science)  # printing science marks
print("English marks:", english)  # printing english marks

print("-------------------------------")
print("Total marks:", total)  # printing total marks
print("Average marks:", averge)  # printing average marks

if averge >= 90:
    print("Grade A")
elif 75 <= averge < 90:
    print("Grade B")
elif 50 <=  averge < 75:
    print("Grade C")
else:
    print("Fail")
