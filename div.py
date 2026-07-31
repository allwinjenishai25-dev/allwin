try:
    a = int(input("Enter the number a : "))
    b = int(input("Enter the number b : "))
    print(a/b)
except ZeroDivisionError:
    print("Zero divition error")
except EnvironmentError:
    print("Environment error")