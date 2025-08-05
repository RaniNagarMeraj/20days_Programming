age=int(input("enter the age:"))
if age >=18:
    print("eleigible to vote")
    if age>=60:
        print(" go to first floor")
    else:
        print("go to third floor")
else:
    print("not eligible to vote")