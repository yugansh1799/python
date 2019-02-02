#if elif else used to check multiple conditions
# 1 to 3(Free)
# 4 to 10(150)
# 11 to60(500)
# abhove 60(1000)

age= input("please input your age ")
age= int(age)
if 0<age<=3:
    print("ticket price : free")
elif 3<age<=10:
     print("ticket price: 150")
elif 10<age<60:
     print("ticket price:500")
else:
        print ("ticket price : 1000")
