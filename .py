marks = []
subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]                                                                        

for sub in subjects:
    m = int(input(f"Enter {sub} marks: "))
    marks.append(m)

#Function	              Purpose
#len(list)	               Count how many elements are in the list
#append(value)	             Add item to the end of the list
#insert(i, x)	            Insert x at index i
#remove()                   Remove first occurrence of a value


#len ()     function 
my_marks = [88, 92, 75, 68, 90, 85]
# Print how many marks are there in the list

print(len(my_marks))



#append() function                                                                                                                      
my_marks = [88, 92, 75]
# Print how many marks are there in the list                                                                        
my_marks.append(80)
print(my_marks)


#insert() function
my_marks = [60, 70, 90]
# Insert 85 at index 2
# Then print the list
my_marks.insert(2,85)
print(my_marks)


#remove() function
my_marks = [55, 65, 75, 85, 95]
# Remove 75 from the list
# Then print the list
my_marks.remove(75)
print(my_marks)
