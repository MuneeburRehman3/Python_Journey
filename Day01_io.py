name = input("enter your name: ")
age = int(input("enter your age: "))
print(f"Hello {name}, next year you will be {age+1} years old")

num1 = float(input("enter 1st number: "))
try:
    num2 = float(input("enter 2nd number: "))
    print(f"the sum of two numbers is: {num1+num2}")
    print(f"the difference of two numbers is: {num1-num2}")
    print(f"the product of two numbers is: {num1*num2}")
    print(f"the division of two numbers is: {num1/num2}")
except ZeroDivisionError:
    print("2nd number cannot be zero")