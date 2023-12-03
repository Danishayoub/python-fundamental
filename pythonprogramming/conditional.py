#first test
'''
age=int(input("please enter age"))
if(age>=18):
    print("you are eligible for vote")
else:
    print("beta ghar jao")
    '''
#second test
''''
x=int(input("Enter first no:"))
y=int(input("Enter Second no:"))
z=int(input("Enter third no:"))
if(x>y and x>z):
    print("The greatest no is:",x)
if(y>x and y>z):
    print("The greatest no is:",y)
if(z>y and z>y):
    print("The greatest no is:",z)
 '''
#Third test
marks=int(input("Enter you marks:"))
if(marks>=30):
    if(marks>=30 and marks<=45):
        print("Third division")
    elif(marks>45 and marks<=59):
        print("Second division ")
    else:
        print("First division")
else:
    print("Your are fail")