age=int(input("enter the age:"))
sex=input("enter the sex of the employee:")
ms=input("enter the marital status as YES or NO:")
if sex=="F":
    print("The employee works only in urban areas")
elif sex=="M" and age>20 and age<=40:
        print("The employee can work anywhere")
elif sex=="M" and age>40 and age<=60:
            print("The employee works in urban areas")
else:
    print("ERROR")
