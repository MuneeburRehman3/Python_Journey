#challenge 1:(Calculate area and classification of a circle)
radius=float(input("Enter the radius of the circle: "))
area=3.14*radius**2
print("The area of the circle is:", area)
if area<50:
    print("The area of the circle is small.")
elif area>=50 and area<=200:
    print("The area of the circle is medium.")
else:
    print("The area of the circle is large.")

#challenge 2:(Age classification)
try:
    age=int(input("Enter your age: "))
    if age>=0 and age<=12:
        print("You are a child.")
    elif age>12 and age<=19:
        print("You are a teenager.")            
    elif age>=20 and age<=59:
        print("You are an adult.")
    elif age>=60:
        print("You are a senior.")
    else:
        print("Invalid age.")
except ValueError:
    print("Please enter a valid age.")

#challenge 3:(Login system)
username=input("Enter your username: ")
password=input("Enter your password: ")
if username=="admin" and password=="password1234":
    print("Login successful.")
else:
    print("Invalid username or password.")    