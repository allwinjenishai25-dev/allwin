a=int(input("Enter your number:"))
b=int(input("Enter your number:"))

choice=input("Enter choice:")

if choice==0:

    Add=(a+b)
    print("sum=",Add)

elif choice==1:

    Sub=(a-b)
    print("sum=",Sub) 

elif  choice==2:

    Mul=(a*b)
    print("sum=",Mul)

elif  choice==3:

    Div=(a/b)
    print("sum=",Div)
else:
    print("invalid choice")