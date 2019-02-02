num=3
factorial=1
if num<0:
    print("sorry fact does not exist")
elif num==0:
    print("the fact is zero")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the fact of",num,"is",factorial)