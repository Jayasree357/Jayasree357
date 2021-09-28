salary=int(input("enter the salary amount of the employee:"))
experience=int(input("enter the year of experience of employee:"))
if experience>5:
    bonus_amount=salary*(5/100)
    print(bonus_amount)
    print(salary+bonus_amount)
