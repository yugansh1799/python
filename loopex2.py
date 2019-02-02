num=input("enter number having more than 2 digits  ")
total=0
i=0
while i < len(num):
    total+=int(num[i])
    i+=1
print(total)   