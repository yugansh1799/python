name, char= input("enter your name and character ").split(",")
print(f"length of your name is {len(name)}")
#print(f"character count {name.count(char)}") #case sensitive.
print(f"character count {name.lower().count(char.lower())}") 
# to make string case insensitive we will convert it lower case .
# Deepansh-deepansh
# E-e
#name.lower().count(char.lower())