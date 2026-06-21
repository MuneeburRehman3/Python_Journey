# Challenge 1: Build a contact book - store 3 names as keys and 
# phone numbers as values
contact_book = {}

while len(contact_book) < 3:
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    contact_book[name] = number

print("\nContact book:")
for name, number in contact_book.items():
    print(f"{name}: {number}")

#challenge 2
student = {"name": "Ali", "age": 21, "course": "CS"}
gettingname=student.get("name")
gettingage=student.get("age")
gettinggrade=student.get("grade","Not Assigned")
print(gettingname)  
print(gettingage)
print(gettinggrade)


#challenge 3 Word frequency counter
sentence = input("Enter a sentence: ")
words = sentence.split()
word_counts = {}
for word in words:
    word_counts[word.lower()] = word_counts.get(word.lower(), 0) + 1    
print("\nWord frequency count:")
print(word_counts)

#Challenge 4 looping through challenge 1 to get all item()
for x,y in contact_book.items():
    print(f"Name: {x}, Number: {y}")



