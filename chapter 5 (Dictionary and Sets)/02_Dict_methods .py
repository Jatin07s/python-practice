marks = {
    "Jatin": 10,
    "Barnak": 42,
    "Garvit": 99,
    "List": [1,2,3],
    0: "sukuna"
}

# print(marks.items()) #returns as tuple
# print(marks.keys()) #returns the keys
# print(marks.values()) #return the values 
# marks.update({"Garvit": 100 , "Hello": [2,3,4]}) #updates the original dict. 
# print(marks)

print(marks.get("Jatin2")) #it gives None , when there is no specific key in the dict otherwise returns the values 
print(marks["Jatin2"]) # its gives error , when there is no specific key in this dict otherwise returns the values


