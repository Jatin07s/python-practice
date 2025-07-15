# Write a program to accept marks pf 6 students and display them in a sorted manner. 


Marks = []

f1 = int(input("Enter the marks here : "))
Marks.append(f1)
f2 = int(input("Enter the marks here : "))
Marks.append(f2)
f3 = int(input("Enter the marks here : "))
Marks.append(f3)
f4 = int(input("Enter the marks here : "))
Marks.append(f4)
f5 = int(input("Enter the marks here : "))
Marks.append(f5)
f6 = int(input("Enter the marks here : "))
Marks.append(f6)

Marks.sort()  #it arranges in ascending order


print(Marks)