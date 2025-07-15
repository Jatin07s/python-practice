a = (1,2,45,3,4,5,45, "rohan", False, "Shivam")

no = a.count(45) #it counts the specific element
print(no)

i = a.index(45)  #it finds the index value from(0,1,2,3...) and gives the index value of the most 1st element either it repeats. 
print(i)

print(len(a))  #to find the length of a tuple

print(2 in a) #used for finding an element in the tuple , like 2 in a , means does 2 present in a tuple or not output = True/False

repeated = a*3
print(repeated)  #a*3 means repeat the existing tuple for 3 times 

# print(max(a)) its showing error cuz in the tuple both str and int values are there , difficult to identify 

b=(1,2,3,4,5,6)
print(max(b))
print(min(b))


print(len(a)) #lenth of tuple

sliced = b[1:4]  #show elements from index 1 to index 3 (just before the 4)
print(sliced)

abc = (1,2,3,4) 
a,b,c,d = abc  #it meeans the elements in the abc are now assigned to a,b,c,d respectively. means a=1 , b=2 , c=3 , d=4 
print(a,b,c,d)

print(d) # d is assigned to 4