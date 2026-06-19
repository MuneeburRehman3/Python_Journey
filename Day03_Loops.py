#challenge no.1
for i in range(1,51):
        if i%2==0:
            print(i)

#challenge no.2
num1=0
total=0
while True:
    user=input("Enter a number: ")
    if user=="stop":
            break
    else:
        num=int(user)
        total+=num
        num1+=1
print(f"The sum of the numbers is: {total}")
print(f"the total numbers entered is: {num1}")   

#challenge no.3
user=input("Enter something: ")
count=0  
I=("a","e","i","o","u")    
for i in user:
    if i in I:
        print(i)
        count+=1
print(f"The number of vowels in the string is: {count}")

#challenge no.4
for i in range(1,1000):
    if i%7==0 and i%13==0:
        print(i)
        break
        


