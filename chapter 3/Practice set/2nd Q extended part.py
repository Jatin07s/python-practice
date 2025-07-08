a = input("Enter the selected Student name : ")

b = int(input("Enter the date of selection :  "))

c = input("Enter the month : ")

d = int(input("Enter the year : "))

e = f"{b} {c} {d}"  #f string is used here , means to add 2 or more strings or int any kind of thing together like in date , day , month year to combine that we use f string 

letter = '''Dear name
             you are selected
             date'''

print(letter.replace("name" , a).replace("date" , e))

