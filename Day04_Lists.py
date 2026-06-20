# Challenge 1: Use slicing to extract first 3, last 2, and every-other number from a list
list1 = [1, 2, 3, 4, 5, 6, 7]
print("First 3:", list1[0:3])
print("Last 2:", list1[-2:])
print("Every other from index 0:", list1[::2])

# Challenge 2: Collect 5 user-entered numbers into a list, then sort and reverse it
number = []
while len(number) < 5:
    num = int(input("enter a number: "))
    number.append(num)

print("\nOriginal list:", number)

number.sort()
print("Sorted list:  ", number)

number.reverse()
print("Reversed list:", number)

# Challenge 3: Manage a daily tasks list - remove, insert, and pop items
tasks = ["wake up", "pray", "study", "gym", "sleep"]
tasks.remove("gym")
tasks.insert(2, "eat")
popped = tasks.pop(-1)
print(popped)
print(tasks)