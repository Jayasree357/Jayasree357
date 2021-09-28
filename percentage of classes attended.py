ch=int(input("enter the number of classes held:"))
ca=int(input("enter the number of classes attended:"))
percent=(ca/ch)*100
print(percent,"%")
if percent<float(75):
    print("The student is not allowed to write the exam")
else:
    print("The student is allowed to write the exam")
        
